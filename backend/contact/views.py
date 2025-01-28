from datetime import datetime

from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from model.models import Model
from .models import Contact
from .serializers import ContactSerializer

import logging

logger = logging.getLogger(__name__)


class ContactAPIView(APIView):
    serializer_class = ContactSerializer

    def get(self, request, id=None):
        if id:
            model = get_object_or_404(Model, id=id)
            return Response(
                {"message": f"Contact page for model {model.full_name}"}
            )
        return Response({"message": "Contact page"})

    def post(self, request, id=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                self._save_contact_request(serializer.validated_data, id)
                self._send_email(serializer.validated_data, id)

                return Response(
                    {"message": "Email sent successfully"},
                    status=status.HTTP_200_OK,
                )
            except Exception as e:
                logger.error(
                    f"Error while processing contact request: {str(e)}"
                )
                return Response(
                    {"error": f"An error occurred: {str(e)}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def _save_contact_request(self, data, id=None):
        name = data.get("name")
        last_name = data.get("last_name")
        phone_number = data.get("phone_number")
        email = data.get("email")
        message = data.get("message")
        model = None

        if id:
            model = get_object_or_404(Model, id=id)

        contact_request = Contact.objects.create(
            name=name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            message=message,
            model=model,
        )
        return contact_request

    def _send_email(self, data, id=None):
        email = data.get("email")
        message = data.get("message")

        if not email or not message:
            raise ValueError("Email and message are required.")

        subject = "Contact Request"
        context = {"message": message}

        if id:
            model = get_object_or_404(Model, id=id)
            subject = f"Model Selection: {model.full_name}"
            context.update(
                {
                    "model": model,
                    "current_year": datetime.now().year,
                }
            )
            template = "email/send_email_with_model.html"
        else:
            template = "email/send_email.html"

        html_content = render_to_string(template, context)
        email_message = EmailMessage(
            subject, html_content, settings.EMAIL_HOST_USER, [email]
        )
        email_message.content_subtype = "html"
        email_message.send()

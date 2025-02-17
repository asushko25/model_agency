from django.test import TestCase, override_settings
from django.core import mail
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from model.models import Model


CONTACT_URL = reverse("contact:contact")


@override_settings(
    # makes running Celery tasks synchronously
    # not send to broker
    CELERY_TASK_ALWAYS_EAGER=True,
    CELERY_TASK_EAGER_PROPAGATES=True,
)
class ContactApiTests(TestCase):
    """
    Test users can contact to model agency about something
    or about specific model
    """
    fixtures = ["seed_data/testing_data_fixture.json"]

    def setUp(self):
        self.client = APIClient()

    def test_contact_page(self):
        """Test user can contact model agency"""
        res = self.client.get(CONTACT_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_post_contact_form(self):
        """Test user can contact model agency"""
        json_data = {
            "name": "TestName",
            "last_name": "TestLastName",
            "email": "test_email@gmail.com",
            "phone_number": "+919667890726",
            "message": "This this test message"

        }
        res = self.client.post(CONTACT_URL, json_data)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        send_mail = mail.outbox[0]
        self.assertIn(
            f"{json_data['name']} {json_data['last_name']}",
            send_mail.body
        )

    def test_post_contact_form_with_model_id(self):
        """Test user can contact model agency about certain model"""
        model = Model.objects.last()
        json_data = {
            "name": "TestName",
            "last_name": "TestLastName",
            "email": "test_email@gmail.com",
            "phone_number": "+919667890726",
            "message": "This this test message"
        }
        contact_url = reverse("contact:contact-with-model", args=[model.id])

        res = self.client.post(
            contact_url, json_data
        )

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        send_mail = mail.outbox[0]
        self.assertIn(
            f"{json_data['name']} {json_data['last_name']}",
            send_mail.body
        )
        self.assertIn(model.full_name, send_mail.body)

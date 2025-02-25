from datetime import timedelta

from django.utils import timezone
from django.conf import settings

from rest_framework import serializers
from rest_framework.serializers import (
    ModelSerializer
)

from .models import (
    NewsLetter,
    NewsLetterSubscriber
)


class NewsLetterSubscriberSerializer(ModelSerializer):
    class Meta:
        model = NewsLetterSubscriber
        fields = ("email",)


class NewsLetterListSerializer(ModelSerializer):
    new_for_subscriber = serializers.SerializerMethodField()

    class Meta:
        model = NewsLetter
        fields = (
            "id", "header", "cover", "caption",
            "created_at", "new_for_subscriber"
        )

    def get_new_for_subscriber(self, obj: NewsLetter) -> bool:
        """
        Returns True if subscriber has newsletters, which are
        going to send to him (and field is called
        `new_for_subscriber` - meaning current newsletter is new
        for current subscriber of newsletter)
        otherwise returns False if user does not have any mails to send to him.
        :param obj:
        :return:
        """
        # user newsletter subscribed date
        subscriber_email = self.context.get(
            settings.COOKIE_NEWS_SUBSCRIBED_EMAIL, None
        )

        # if user is not subscribed we ignore it
        if not subscriber_email:
            return False

        return NewsLetterSubscriber.objects.filter(
            email=subscriber_email, newsletters_to_send=obj
        ).exists()

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
    is_new = serializers.SerializerMethodField()

    class Meta:
        model = NewsLetter
        fields = (
            "id", "header", "cover", "caption",
            "created_at", "is_new"
        )

    def get_is_new(self, obj: NewsLetter) -> bool:
        """
        Newsletters created in a current weekend will have
        field `is_new = True` for users which has subscribed to
        receive newsletters emails. `is_new=True` will be available only at the
        end of week relative to subscribed day.

        For example if user subs to newsletter at 2025.02.02 then
        `is_new` will be available at 2025.02.09,
        and it will be set for newsletters that were created
        during week relative to day use subs.

        By doing that we are letting user know which
        newsletters are new this week.
        :param obj:
        :return:
        """
        # user newsletter subscribed date
        subscribed_at = self.context.get(
            settings.COOKIE_NEWS_SUBSCRIBED_DATA, None
        )

        # if user is not subscribed we ignore it
        if not subscribed_at:
            return False

        if isinstance(subscribed_at, str):
            subscribed_at = timezone.datetime.strptime(
                subscribed_at, "%Y-%m-%d"
            )

        curr_date = timezone.now().date()
        day_since_subs = curr_date - subscribed_at.date()

        # we are marking as `new` if 7 days pass relative to
        # subscribed date
        if day_since_subs.days % 7 != 0:
            return False

        start_curr_week = curr_date - timedelta(days=7)

        #  if newsletter is in range of current start of week relative to
        # subscription date and end of this week relative to  subscription date
        return start_curr_week <= obj.created_at <= curr_date

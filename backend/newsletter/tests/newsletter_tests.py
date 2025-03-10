from django.test import (
    TestCase,
    override_settings
)
from django.core import mail
from django.core.files import File
from django.urls import reverse
from django.conf import settings
from django.utils.timezone import datetime
from datetime import timedelta

from freezegun import freeze_time

from unittest.mock import patch

import tempfile
from typing import Callable

from PIL import Image

from rest_framework.test import APIClient
from rest_framework import status

from newsletter.models import (
    NewsLetter,
    NewsLetterSubscriber
)
from newsletter.serializers import (
    NewsLetterListSerializer
)

try:
    from newsletter.tasks import send_emails_to_newsletter_subscribers
except ImportError:
    raise ImportError(
        "send_emails_to_newsletter_subscribercs was used in testing."
        " Change import statement to refer to celery task which sends"
        " newsletters to subscribers"
    )

NEWSLETTER_URL = reverse("newsletter:newsletter-list")
SIGN_NEWSLETTER_URL = reverse("newsletter:newsletter-sign")

# pagination query value
LIMIT = 2


def sign_to_newsletter() -> NewsLetterSubscriber:
    return NewsLetterSubscriber.objects.create(
        email="testemail@gmail.com"
    )


def freeze_subscribed_date(func: Callable) -> Callable:
    """
    When testing newsletters subscribers we have 3 stages:
    1: Creating newsletter subscriber depending on global variable
    settings.NEWSLETTER_EMAIL_EVERY_NUM_DAY
    2: Creating one newsletter in day
    NEWSLETTER_EMAIL_EVERY_NUM_DAY // 2

    Those 2 steps this decorators take care next steps tests are going
    to implement it
    :param func:
    :return:
    """
    def test_wrapper(*args, **kwargs):
        # 1 stage
        freezer = freeze_time(
            str(
                datetime.now().date()
                - timedelta(
                    days=settings.NEWSLETTER_EMAIL_EVERY_NUM_DAY
                )
            )
        )
        freezer.start()
        subscriber = sign_to_newsletter()
        freezer.stop()

        # 2 stage
        freezer = freeze_time(
            datetime.now().date()
            - timedelta(
                days=settings.NEWSLETTER_EMAIL_EVERY_NUM_DAY // 2
            )
        )
        freezer.start()

        # We need newsletter cover because it will be rendered
        # on mail HTML page
        with tempfile.NamedTemporaryFile(suffix=".jpg") as ntf:
            img = Image.new("RGB", (10, 10))
            img.save(ntf, format="JPEG")
            ntf.seek(0)

            newsletter = NewsLetter.objects.create(
                header="Freezed Newsletter",
                cover=File(ntf),
                caption="Freezed Newsletter Caption",
            )

        freezer.stop()

        # 3 stage, passing newsletter for testing
        func(newsletter=newsletter, subscriber=subscriber, *args, **kwargs)

    return test_wrapper


@override_settings(
    # makes running Celery tasks synchronously
    # not send to broker
    CELERY_TASK_ALWAYS_EAGER=True,
    CELERY_TASK_EAGER_PROPAGATES=True,
)
class NewsLetterApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_newsletter_list(self):
        NewsLetter.objects.create(
            header="Test header",
            caption="Test caption",
        )

        res = self.client.get(NEWSLETTER_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        serializer = NewsLetterListSerializer(
            NewsLetter.objects.all(), many=True
        )

        self.assertEqual(res.data["results"] or res.data, serializer.data)

    # Mock the default_limit to 2
    @patch("paginations.CustomPagination.default_limit", LIMIT)
    def test_newsletter_list_pagination_work(self):
        for i in range(6):
            NewsLetter.objects.create(
                header=f"Test header {i}",
                caption=f"Test caption {i}",
            )

        res = self.client.get(
            NEWSLETTER_URL,
            {"limit": LIMIT, "offset": LIMIT}  # second page
        )

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn("results", res.data)
        self.assertIn("next", res.data)
        self.assertIn("previous", res.data)

        exp_data = NewsLetter.objects.all()[LIMIT:LIMIT + LIMIT]
        serializer = NewsLetterListSerializer(
            exp_data, many=True
        )

        self.assertEqual(res.data["results"], serializer.data)

    def test_sign_to_newsletter(self):
        """
        Test user can sign to receive newsletter mails
        :return:
        """
        data = {
            "email": "testemail@gmail.com"
        }

        res = self.client.post(SIGN_NEWSLETTER_URL, data=data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            data["email"],
            NewsLetterSubscriber.objects.get(email=data["email"]).email
        )

    @freeze_subscribed_date
    def test_subscriber_receives_mails_in_terms(
            self, newsletter: NewsLetter, subscriber: NewsLetterSubscriber
    ):
        send_emails_to_newsletter_subscribers.apply()

        self.assertEqual(len(mail.outbox), 1)

        send_mail = mail.outbox[0]

        self.assertIn(newsletter.header, send_mail.body)
        self.assertIn(newsletter.caption, send_mail.body)

    @freeze_subscribed_date
    def test_subscriber_receives_no_newsletters_mails_invalid_terms(
            self, newsletter: NewsLetter, subscriber: NewsLetterSubscriber
    ):
        for day in range(1, settings.NEWSLETTER_EMAIL_EVERY_NUM_DAY):
            with freeze_time(
                    subscriber.subscribed_at + timedelta(days=day)
            ):
                send_emails_to_newsletter_subscribers.apply()
                self.assertEqual(len(mail.outbox), 0)

    @freeze_subscribed_date
    def test_subscriber_receives_newsletter_expire_subscription_mail(
            self, newsletter: NewsLetter, subscriber: NewsLetterSubscriber
    ):
        """
        Day before subscriber expiration day we send mail about it.
        :param newsletter:
        :param subscriber:
        :return:
        """
        with freeze_time(
            subscriber.expires_at - timedelta(days=1)
        ):
            send_emails_to_newsletter_subscribers.apply()

            self.assertTrue(len(mail.outbox) >= 1)
            self.assertIn(
                "Subscription is Expiring Soon",
                mail.outbox[0].body
            )

    @freeze_subscribed_date
    def test_expire_subscriber_active_false(
            self, newsletter: NewsLetter, subscriber: NewsLetterSubscriber
    ):
        """
        Subscription has expired mark subscriber as inactive
        :param newsletter:
        :param subscriber:
        :return:
        """
        with freeze_time(
                subscriber.expires_at + timedelta(days=1)
        ):
            send_emails_to_newsletter_subscribers.apply()

            self.assertEqual(len(mail.outbox), 0)

            subscriber.refresh_from_db()

            self.assertEqual(subscriber.is_active, False)

    @freeze_subscribed_date
    def test_expire_subscriber_not_receives_mail(
            self, newsletter: NewsLetter, subscriber: NewsLetterSubscriber
    ):
        """
        Subscription has expired, inactive subscriber should receive mails
        :param newsletter:
        :param subscriber:
        :return:
        """
        # Total number of days the subscriber was subscribed before expiring
        total_mails_sent = (
            subscriber.expires_at
            - subscriber.subscribed_at
        ).days

        # Compute the next scheduled email date AFTER expiration
        next_scheduled_email_date = (subscriber.expires_at + timedelta(
            days=settings.NEWSLETTER_EMAIL_EVERY_NUM_DAY - (
                total_mails_sent % settings.NEWSLETTER_EMAIL_EVERY_NUM_DAY
            )
        ))

        with freeze_time(next_scheduled_email_date):
            send_emails_to_newsletter_subscribers.apply()

            self.assertEqual(len(mail.outbox), 0)

            subscriber.refresh_from_db()

            self.assertEqual(subscriber.is_active, False)

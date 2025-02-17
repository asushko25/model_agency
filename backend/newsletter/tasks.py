import logging

from celery import shared_task

from datetime import timedelta

from django.urls import reverse
from django.template.loader import render_to_string
from django.core.mail import send_mass_mail
from django.conf import settings
from django.utils import timezone

from .models import NewsLetterSubscriber, NewsLetter


logger = logging.getLogger("mail_logging")


@shared_task
def send_emails_to_newsletter_subscribercs():
    """
    Send emails to users subscribed to newsletters.
    This runs every `settings.NEWSLETTER_EMAIL_EVERY_NUM_DAY` days.
    """
    subscribers = NewsLetterSubscriber.objects.prefetch_related(
        "newsletters_to_send"
    ).iterator(chunk_size=1000)
    mails_body = []
    expired_subscribers = []

    for subscriber in subscribers:

        # Check if subscription expires
        expire_mail = check_expire_date(subscriber)
        if expire_mail:
            mails_body.append(expire_mail)

        # Check if it's time to send newsletters
        if time_to_send(subscriber):
            newsletters_to_send(subscriber)  # Update subscriber's newsletters

            if subscriber.newsletters_to_send.exists():
                mails_body.append(create_mail_body(subscriber))

        # Mark expired subscriptions for batch update
        if subscriber.expires_at <= timezone.now().date():
            subscriber.is_active = False
            expired_subscribers.append(subscriber)

    # Bulk update expired subscribers
    if expired_subscribers:
        NewsLetterSubscriber.objects.bulk_update(
            expired_subscribers, ["is_active"]
        )

    # Send all emails at once
    if mails_body:
        total_emails = len(mails_body)
        send_count = send_mass_mail(mails_body, fail_silently=True)

        fail_count = total_emails - send_count
        if fail_count > 0:
            logger.error(
                f"Fail to send {fail_count} of mails out of {total_emails}"
            )
        else:
            logger.info(
                "All mails sent successfully!!!"
            )


def create_mail_body(
        subscriber: NewsLetterSubscriber
) -> tuple[str, str, str, list[str]]:
    """
    Creates the email content for newsletter notifications.
    """
    newsletters = subscriber.newsletters_to_send.all()
    context = {
        "newsletter": newsletters[0] if newsletters else None,
        "num_of_newsletters": len(newsletters),
        "newsletters_url": reverse("newsletter:newsletter-list"),
        "main_page_url": reverse("model:main-list"),
        "newsletter_creation_range_days": (
            settings.NEWSLETTER_EMAIL_EVERY_NUM_DAY
        )
    }
    html_content = render_to_string("emails/newsletters_email.html", context)
    return (
        "Model Agency Newsletters", html_content,
        settings.EMAIL_HOST_USER, [subscriber.email]
    )


def check_expire_date(
        subscriber: NewsLetterSubscriber
) -> tuple[str, str, str, list[str]] | None:
    """
    Checks if the subscription is about to expire and notifies the user.
    """
    if subscriber.expires_at - timedelta(days=1) == timezone.now().date():
        return (
            "Your Newsletter subscription at Model Agency"
            f" will end on {subscriber.expires_at}",
            render_to_string("emails/newsletter_expire.html", {
                "main_page_url": reverse("model:main-list"),
                "sign_to_newsletter_url": reverse(
                    "newsletter:newsletter-sign"
                ),
                "expires_at": subscriber.expires_at
            }),
            settings.EMAIL_HOST_USER,
            [subscriber.email]
        )
    return None


def time_to_send(subscriber: NewsLetterSubscriber) -> bool:
    curr_date = timezone.now().date()
    day_since_subs = curr_date - subscriber.subscribed_at

    # if it is not time to send and user is subscribed
    # return false else true
    return (
        day_since_subs.days
        % settings.NEWSLETTER_EMAIL_EVERY_NUM_DAY == 0
        and subscriber.is_active
    )


def newsletters_to_send(subscriber: NewsLetterSubscriber) -> None:
    """
    Update NewsLetterSubscriber.newsletters_to_send with newsletter
    to send today.

    For example if user subs to newsletter at 2025.02.02 and
    settings.NEWSLETTER_EMAIL_EVERY_NUM_DAY = 7 (every week) then
    then email will be send at 2025.02.09 and newsletter which where
    created in range from 2025.02.02 to 2025.02.09, will be added to
    NewsLetterSubscriber.newsletters_to_send and old ones remove it.

    By doing that we are letting server know which
    newsletters are new this week for current subscriber.
    :param subscriber: NewsLetterSubscriber
    :return:
    """
    curr_date = timezone.now().date()

    start_curr_week = curr_date - timedelta(
        days=settings.NEWSLETTER_EMAIL_EVERY_NUM_DAY
    )

    # get newsletters created in NEWSLETTER_EMAIL_EVERY_NUM_DAY
    # relative to when user has subscribed
    new_newsletters = NewsLetter.objects.filter(
        created_at__gte=start_curr_week,
        created_at__lte=curr_date
    )
    # add new newsletters to subscriber and removes old ones
    subscriber.newsletters_to_send.set(new_newsletters)

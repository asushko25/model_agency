import logging

from celery import shared_task

import smtplib

from django.core.mail.message import EmailMessage

logger = logging.getLogger("mail_logging")


@shared_task
def send_contact_email(
        subject: str,
        html_content: str,
        from_email: str,
        to_emails: list[str]
) -> None:
    """
    Send mail notification to user that we will contact him.
    :param subject:
    :param html_content:
    :param from_email:
    :param to_emails:
    :return:
    """
    email_message = EmailMessage(
        subject, html_content, from_email, to_emails
    )
    email_message.content_subtype = "html"

    try:
        email_message.send()
    except smtplib.SMTPException as e:
        logger.error(f"Problem with a SMPT: {e}")
    except Exception as e:
        logger.error(f"Unexpected issues when sending contact email: {e}")

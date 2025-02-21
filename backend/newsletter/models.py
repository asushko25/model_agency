import os
import uuid
from datetime import timedelta

from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext as _


class NewsLetterSubscriber(models.Model):
    email = models.EmailField(_("Email address"), unique=True)
    subscribed_at = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True, db_index=True)
    newsletters_to_send = models.ManyToManyField(
        "NewsLetter",
        related_name="newsletters",
    )

    @property
    def expires_at(self) -> timezone.datetime.date:
        """
        Returns date when user subscription ends.
        Base on when record was created and value in
        settings.COOKIE_EXPIRE_SUBSCRIBED_DATA
        :return:
        """
        return self.subscribed_at + timedelta(
            seconds=settings.COOKIE_EXPIRE_SUBSCRIBED_DATA
        )

    class Meta:
        ordering = ["-id"]
        verbose_name = "NewsLetter Subscriber"
        verbose_name_plural = "NewsLetter Subscribers"


def news_letter_image_cover(instance: "NewsLetter", filename: str):
    _, extension = os.path.splitext(filename)

    filename = (
        f"-{uuid.uuid4()}{instance.id}{extension}"
    )
    full_path = os.path.join(
        "uploads",
        "newsletter",
        filename,
    )

    return full_path


class NewsLetter(models.Model):
    header = models.CharField(max_length=255)
    cover = models.ImageField(upload_to=news_letter_image_cover)
    caption = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]

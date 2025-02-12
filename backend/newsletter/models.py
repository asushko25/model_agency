import os
import uuid

from django.db import models
from django.utils.translation import gettext as _


class NewsLetterSubscriber(models.Model):
    email = models.EmailField(_("Email address"), unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, db_index=True)

    class Meta:
        ordering = ["-id"]
        verbose_name = "News Letter Subscriber"
        verbose_name_plural = "News Letter Subscribers"


def news_letter_image_cover(instance: "NewsLetter", filename: str):
    _, extension = os.path.splitext(filename)

    filename = (
        f"-{uuid.uuid4()}{instance.id}.{extension}"
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

    class Meta:
        ordering = ["-id"]
        verbose_name = "News Letter"
        verbose_name_plural = "News Letters"

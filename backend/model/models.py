import os
import uuid
import logging

from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext as _

from phonenumber_field.modelfields import PhoneNumberField

logger = logging.getLogger("model_app")


class UserManager(BaseUserManager):
    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        extra_fields.setdefault("full_name", "Admin")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    phone_number = PhoneNumberField(max_length=15, blank=True, null=True)
    full_name = models.CharField(max_length=255, db_index=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]

    def __str__(self):
        return f"{self.full_name} ({self.email})"

    class Meta:
        ordering = ["-id"]
        verbose_name = "User"
        verbose_name_plural = "Users"


class Model(models.Model):
    model_user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="models",
    )
    date_of_birth = models.DateField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    height = models.PositiveIntegerField()

    HAIR_CHOICES = [
        ("blonde", "Blonde"),
        ("brown", "Brown"),
        ("black", "Black"),
        ("red", "Red"),
        ("grey", "Gray"),
        ("other", "Other"),
    ]
    hair = models.CharField(max_length=20, choices=HAIR_CHOICES)

    EYE_COLOR_CHOICES = [
        ("blue", "Blue"),
        ("green", "Green"),
        ("brown", "Brown"),
        ("gray", "Gray"),
        ("hazel", "Hazel"),
    ]
    eye_color = models.CharField(max_length=10, choices=EYE_COLOR_CHOICES)

    GENDER_CHOICES = [
        ("man", "Man"),
        ("woman", "Woman"),
    ]
    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
        default="woman",
        blank=False,
        null=False,
    )
    bust = models.PositiveIntegerField()
    waist = models.PositiveIntegerField()
    hips = models.PositiveIntegerField()

    def __str__(self):
        return self.model_user.full_name

    @property
    def full_name(self):
        return self.model_user.full_name


def model_image_file_path(instance: "ModelImages", filename: str):
    _, extension = os.path.splitext(filename)
    first_name, last_name = instance.model.full_name.split(" ")

    filename = (
        f"{slugify(first_name)}"
        f"-{slugify(last_name)}"
        f"-{uuid.uuid4()}.{extension}"
    )
    full_path = os.path.join(
        "uploads",
        "models",
        f"{instance.model.gender}",
        filename,
    )

    logger.info(f"{first_name} {last_name} image path {full_path}")

    return full_path


class ModelImages(models.Model):
    model = models.ForeignKey(
        Model, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to=model_image_file_path)
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.model.full_name}: {self.image.name}"

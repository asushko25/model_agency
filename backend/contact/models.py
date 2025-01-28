from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from model.models import Model


class Contact(models.Model):
    model = models.ForeignKey(
        Model,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="contacts",
    )
    name = models.CharField(verbose_name="Name", max_length=100)
    last_name = models.CharField(
        verbose_name="Last Name",
        max_length=100
    )
    email = models.EmailField(verbose_name="Email Address", )
    phone_number = PhoneNumberField(verbose_name="Phone Number")
    message = models.TextField(verbose_name="Message",)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Submitted At"
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return f"Contact: {self.full_name} ({self.email})"

    @property
    def full_name(self):
        return f"{self.name} {self.last_name}"

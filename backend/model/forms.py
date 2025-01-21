from django import forms
from .models import User


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", "full_name", "phone_number")

    def clean_password(self):
        return None

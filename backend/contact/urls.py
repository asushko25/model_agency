from django.urls import path
from .views import ContactAPIView

urlpatterns = [
    path(
        "<int:id>/", ContactAPIView.as_view(), name="contact-with-model"
    ),
    path("", ContactAPIView.as_view(), name="contact"),
]

app_name = "contact"

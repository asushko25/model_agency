from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NewsLetterViewSet

router = DefaultRouter()
router.register("", NewsLetterViewSet, "newsletter")

urlpatterns = [
    path("", include(router.urls))
]

app_name = "newsletter"

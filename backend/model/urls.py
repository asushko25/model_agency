from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ManModelViewSet, WomanModelViewSet, MainViewSet

router = DefaultRouter()
router.register("main", MainViewSet, basename="main")
router.register("man", ManModelViewSet, basename="man")
router.register("woman", WomanModelViewSet, basename="woman")

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "model"

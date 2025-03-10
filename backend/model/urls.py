from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ManModelViewSet, WomanModelViewSet, MainViewSet

router = DefaultRouter()
router.register("main", MainViewSet, basename="main")
router.register("men", ManModelViewSet, basename="men")
router.register("women", WomanModelViewSet, basename="women")

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "model"

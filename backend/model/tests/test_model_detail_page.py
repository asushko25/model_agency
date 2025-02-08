import logging

from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

from ..models import Model
from ..serializers import (
    WomanModelDetailSerializer,
    ManModelDetailSerializer
)
from .utils.model_test_util import (
    model_detail_url,
)

logger = logging.getLogger("model.tests")


class DetailPageApiTests(TestCase):
    """Test Model detail page functionality"""
    logger.info("TESTING Detail Model page!!!!")

    def setUp(self) -> None:
        self.client = APIClient()

        self.user = get_user_model().objects.create(
            email="test1@gmail.com", full_name="Test Testing"
        )
        self.model = Model.objects.create(
            model_user=self.user,
            date_of_birth="2000-01-01",
            city="City1",
            country="Country1",
            height=180,
            hair="blonde",
            eye_color="blue",
            gender="woman",
            bust=110,
            waist=90,
            hips=105,
        )

    def test_man_detail_page_model(self):
        res = self.client.get(
            model_detail_url(self.model.id, self.model.gender)
        )

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        serializer = ManModelDetailSerializer(self.model)

        self.assertEqual(res.data, serializer.data)
        self.assertIn(
            "contact_url",
            res.data,


        )
        self.assertIn(
            str(self.model.id),
            res.data["contact_url"],
            "Url to Contact page from Detail Model page should pass model id"
        )

    def test_woman_detail_page_model(self):
        self.model.gender = "woman"
        res = self.client.get(
            model_detail_url(self.model.id, self.model.gender)
        )

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        serializer = WomanModelDetailSerializer(self.model)

        self.assertEqual(
            res.data,
            serializer.data,
            "Detail Model JSON body response should have `contact_url` in body"
        )
        self.assertIn("contact_url", res.data)
        self.assertIn(
            str(self.model.id),
            res.data["contact_url"],
            "Url to Contact page from Detail Model page should pass model id"
        )

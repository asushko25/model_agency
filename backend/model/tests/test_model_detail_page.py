from django.test import TestCase
from django.conf import settings

from rest_framework.test import APIClient
from rest_framework import status

from ..models import Model
from ..serializers import ModelDetailSerializer
from .utils.model_test_util import (
    model_detail_url,
)


class DetailPageApiTests(TestCase):
    """Test Model detail page functionality"""

    def setUp(self) -> None:
        self.client = APIClient()

        self.user = settings.AUTH_USER_MODEL.objects.create(
            email="test1@gmail.com", full_name="Test Testing"
        )
        self.model = Model.objects.create(
            model_user=self.user,
            date_of_birth="2000-01-01",
            city="City1",
            country="Country1",
            height=180,
            hair="black",
            eye_color="blue",
            gender="woman",
            bust=110,
            waist=90,
            hips=105,
        )

    def test_detail_page_model(self):
        res = self.client.get(model_detail_url(self.model.id))

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        serializer = ModelDetailSerializer(self.model)

        self.assertEqual(res.data, serializer.data)
        self.assertIn("contact_url", res.data)

    def test_detail_page_has_contact_url(self):
        """
        Test Model Detail page in response has field 'contact_url'
        and also valid
        """
        res = self.client.get(model_detail_url(self.model.id))
        contact_res = self.client.get(res.data["contact_url"])

        self.assertEqual(contact_res.status_code, status.HTTP_200_OK)

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status
#
# from model.serializer import (
#
# )
# from model.models import Model

MODEL_LIST_URL = ""


class UnauthenticatedApiTests(TestCase):
    """Test unauthenticated users can enter to all endpoints"""
    def setUp(self) -> None:
        self.client = APIClient()

    def request_object(self):
        return self.client.get(MODEL_LIST_URL).wsgi_request

    def test_model_list(self):
        """TEST Main page. Should return man and woman models"""
        pass

    def test_search_by_credentials_in_model_list(self):
        pass

    def test_filter_model_list_by_country(self):
        pass

    def test_filter_model_list_by_height(self):
        pass

    def test_filter_model_list_by_eyes(self):
        pass

    def test_filter_model_list_by_bust(self):
        pass

    def test_filter_model_list_by_waist(self):
        pass

    def test_man_model_list(self):
        pass

    def test_woman_model_list(self):
        pass

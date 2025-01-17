from django.test import TestCase
from django.urls import reverse


from rest_framework.test import APIClient
from rest_framework import status

from ..models import Model
from .utils.model_test_util import (
    paginated_data_or_not,
    UtilSerializingModels,
)


MAIN_LIST_URL = reverse("model:model-list")


class MainPageApiTests(TestCase):
    """Test unauthenticated users can enter to Main page"""
    # Loads testing data, 10 users, 5 man, 5 woman models
    # without images
    fixtures = ["seed_data/testing_data_fixture.json"]

    def setUp(self) -> None:
        self.client = APIClient()

        # Class for handling common serializing of models
        self.main_util = UtilSerializingModels(
            limit=6, offset=0
        )

    def test_model_list(self):
        """TEST Main page. Should return man and woman models"""
        res = self.client.get(MAIN_LIST_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        res_data = paginated_data_or_not(res.data)
        self.assertEqual(
            res_data, self.main_util.serializing_list_of_models()
        )

    def test_models_list_with_pagination(self):
        """Test main page on pagination button 'Show More'"""

        # get 2 page
        limit = self.main_util.limit
        offset = self.main_util.offset = limit

        res = self.client.get(
            MAIN_LIST_URL,
            {"limit": limit, "offset": offset}
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        res_data = paginated_data_or_not(res.data)
        self.assertEqual(
            res_data, self.main_util.serializing_list_of_models()
        )

    def test_search_by_credentials_in_model_list(self):
        """Test Main page search form by model fullname"""
        # TODO: talk with backend developer about full_name
        model_fullname = Model.objects.last().model_user.full_name
        partially_fullname = model_fullname[:len(model_fullname) // 2]

        res = self.client.get(
            MAIN_LIST_URL,
            {"search": partially_fullname}
        )

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        res_data = paginated_data_or_not(res.data)
        exp_data = self.main_util.serializing_list_of_searched_models(
            search=partially_fullname
        )

        self.assertEqual(res_data, exp_data)

    def test_search_by_credentials_no_result_found(self):
        """
        Test Main page search query parameter by model fullname
        returns 'No result found' with 200 status
        """
        search_none = "a124?None"
        res = self.client.get(
            MAIN_LIST_URL,
            {"search": search_none}
        )

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        res_data = paginated_data_or_not(res.data)
        exp_data = self.main_util.serializing_list_of_searched_models(
            search=search_none
        )

        self.assertEqual(res_data, exp_data)

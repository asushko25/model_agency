import logging

from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch


from rest_framework.test import APIClient
from rest_framework import status

from model.models import Model
from .utils.model_test_util import (
    paginated_data_or_not,
    model_detail_url,
    UtilFilterSearchSerialize,
)


MAIN_LIST_URL = reverse("model:main-list")

# Pagination limits and offset for "More"
# pagination button
LIMIT = 2
OFFSET = 0

logger = logging.getLogger("model.tests")


@patch("model.views.CustomPagination.default_limit", LIMIT)  # Mock the default_limit to 2
class MainPageApiTests(TestCase):
    """Test unauthenticated users can enter to Main page"""
    logger.info("TESTING Main page!!!!")

    # Loads testing data, 10 users, 5 man, 5 woman models
    # without images
    fixtures = ["seed_data/testing_data_fixture.json"]

    def setUp(self) -> None:
        self.client = APIClient()

        # Class for handling common serializing of models
        self.main_util = UtilFilterSearchSerialize(
            limit=LIMIT, offset=OFFSET
        )

    def test_pagination_exist(self):
        res = self.client.get(MAIN_LIST_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        error_message = (
            "Pagination should be on Woman page model list"
        )
        self.assertIn("next", res.data, error_message)
        self.assertIn("previous", res.data, error_message)
        self.assertIn("results", res.data, error_message)

    def test_model_list(self):
        """TEST Main page. Should return man and woman models"""
        res = self.client.get(MAIN_LIST_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        res_data = paginated_data_or_not(res.data)
        exp_data = self.main_util.serializing_list_of_models(
                request=res.wsgi_request
        )

        self.assertEqual(
            res_data, exp_data
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
            res_data, self.main_util.serializing_list_of_models(
                request=res.wsgi_request
            )
        )

    def test_search_by_credentials_in_model_list(self):
        """Test Main page search form by model fullname"""
        model_fullname = Model.objects.last().model_user.full_name
        partially_fullname = model_fullname[:len(model_fullname) // 2]

        res = self.client.get(
            MAIN_LIST_URL,
            {"search": partially_fullname}
        )

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        res_data = paginated_data_or_not(res.data)
        exp_data = self.main_util.serializing_list_of_searched_models(
            search=partially_fullname, request=res.wsgi_request
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

    def test_each_model_has_url_to_detail_page(self):
        """
        Test Main page. Where for each model json body also will be
        URL to their Model Detail page
        """
        res = self.client.get(MAIN_LIST_URL)
        model = paginated_data_or_not(res.data)[0]
        error_message = (
            "Each JSON Model Body should have `detail_url` on Main page"
        )

        self.assertIn("detail_url", model, error_message)

        detail_res = self.client.get(model_detail_url(model["id"]))

        self.assertEqual(detail_res.status_code, status.HTTP_200_OK)

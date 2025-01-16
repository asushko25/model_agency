from django.test import TestCase
from django.urls import reverse


from rest_framework.test import APIClient
from rest_framework import status

from backend.model.models import Model
from backend.tests.utils.model_test_util import (
    paginated_data_or_not,
    UtilSerializingModels,
    UtilFilterSearchSerialize
)


MAIN_LIST_URL = reverse("")
MAN_LIST_PAGE_URL = reverse("")
WOMAN_LIST_PAGE_URL = reverse("")


class UnauthenticatedMainPageApiTests(TestCase):
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


class UnauthenticatedManPageApiTests(TestCase):
    """Test unauthenticated users can enter man endpoint"""
    # Loads testing data, 10 users, 5 man, 5 woman models
    # without images
    fixtures = ["seed_data/testing_data_fixture.json"]

    def setUp(self) -> None:
        self.client = APIClient()

        # Class for handling common serializing of models
        self.man_util = UtilFilterSearchSerialize(
            limit=12, offset=0, gender="man"
        )

    def test_man_model_list(self):
        """TEST Man page. Should return male models"""
        res = self.client.get(MAN_LIST_PAGE_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        res_data = paginated_data_or_not(res.data)
        man_models = Model.objects.filter(
            gender="man"
        )

        self.assertEqual(
            res_data,
            self.man_util.serializing_list_of_models(
                data=man_models
            )
        )

    def test_man_models_list_with_pagination(self):
        """Test man page on pagination button 'Show More'"""

        # get 2 page
        limit = self.man_util.limit
        offset = self.man_util.offset = limit

        res = self.client.get(
            MAIN_LIST_URL,
            {"limit": limit, "offset": offset}
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        res_data = paginated_data_or_not(res.data)
        self.assertEqual(
            res_data, self.man_util.serializing_list_of_models()
        )

    def test_search_by_credentials_in_man_list(self):
        """Test Man page search form by man model fullname"""
        # TODO: talk with backend developer about full_name
        model_fullname = Model.objects.filter(gender="man").last().full_name
        partially_fullname = model_fullname[:len(model_fullname) // 2]

        res = self.client.get(
            MAIN_LIST_URL,
            {"search": partially_fullname}
        )

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        res_data = paginated_data_or_not(res.data)
        exp_data = self.man_util.serializing_list_of_searched_models(
            search=partially_fullname
        )

        self.assertEqual(res_data, exp_data)

    def test_range_type_field_filters(self):
        """
        Test Man page  filters to range type fields
         like "height", "bust", "waist", "hips"
         which need from_{} and to_{} in query parameters
        """
        range_field = ["height", "bust", "waist", "hips"]
        model = Model.objects.filter(gender="man").last()

        for field in range_field:
            # get model parameter
            model_param = getattr(model, field)

            # make model parameters range bigger to
            # include more models
            from_ = model_param - 10
            to_ = model_param + 10

            res = self.client.get(
                MAN_LIST_PAGE_URL,
                {
                    f"from_{field}": from_,
                    f"to_{field}": to_
                }
            )

            self.assertEqual(res.status_code, status.HTTP_200_OK)

            res_data = paginated_data_or_not(res)
            exp_data = self.man_util.filter_by_field_range(
                from_=from_, to_=to_, field=field
            )

            self.assertEqual(res_data, exp_data)

    def test_choice_type_field_filters(self):
        """
        Test Man page  filters to choice type fields
        like "hair", "eye" which need from_{} and to_{}
        in query parameters
        """
        choices_field = ["hair", "eye"]
        model = Model.objects.filter(gender="man").last()

        for field in choices_field:
            # get model parameter
            model_param = getattr(model, field)

            res = self.client.get(
                MAN_LIST_PAGE_URL,
                {f"{field}": model_param}
            )

            self.assertEqual(res.status_code, status.HTTP_200_OK)

            res_data = paginated_data_or_not(res)
            exp_data = self.man_util.filter_by_choice_field(
                field=field, value=model_param
            )

            self.assertEqual(res_data, exp_data)


class UnauthenticatedWomanPageApiTests(TestCase):
    """Test unauthenticated users can enter woman endpoint"""
    # Loads testing data, 10 users, 5 man, 5 woman models
    # without images
    fixtures = ["seed_data/testing_data_fixture.json"]

    def setUp(self) -> None:
        self.client = APIClient()

        # Class for handling common serializing of models
        self.woman_util = UtilFilterSearchSerialize(
            limit=12, offset=0, gender="gender"
        )

    def test_woman_model_list(self):
        """TEST Woman page. Should return female models"""
        res = self.client.get(WOMAN_LIST_PAGE_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        res_data = paginated_data_or_not(res.data)
        woman_models = Model.objects.filter(
            gender="woman"
        )

        self.assertEqual(
            res_data,
            self.woman_util.serializing_list_of_models(
                data=woman_models
            )
        )

    def test_woman_models_list_with_pagination(self):
        """Test Woman page on pagination button 'Show More'"""

        # get 2 page
        limit = self.woman_util.limit
        offset = self.woman_util.offset = limit

        res = self.client.get(
            WOMAN_LIST_PAGE_URL,
            {"limit": limit, "offset": offset}
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        res_data = paginated_data_or_not(res.data)
        self.assertEqual(
            res_data, self.woman_util.serializing_list_of_models()
        )

    def test_search_by_credentials_in_woman_list(self):
        """Test Woman page search query param by woman model fullname"""
        # TODO: talk with backend developer about full_name
        model_fullname = Model.objects.filter(gender="woman").last().full_name
        partially_fullname = model_fullname[:len(model_fullname) // 2]

        res = self.client.get(
            WOMAN_LIST_PAGE_URL,
            {"search": partially_fullname}
        )

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        res_data = paginated_data_or_not(res.data)
        exp_data = self.woman_util.serializing_list_of_searched_models(
            search=partially_fullname
        )

        self.assertEqual(res_data, exp_data)

    def test_range_type_field_filters(self):
        """
        Test Man page  filters to range type fields
         like "height", "bust", "waist", "hips"
         which need from_{} and to_{} in query parameters
        """
        range_field = ["height", "bust", "waist", "hips"]
        model = Model.objects.filter(gender="woman").last()

        for field in range_field:
            # get model parameter
            model_param = getattr(model, field)

            # make model parameters range bigger to
            # include more models
            from_ = model_param - 10
            to_ = model_param + 10

            res = self.client.get(
                WOMAN_LIST_PAGE_URL,
                {
                    f"from_{field}": from_,
                    f"to_{field}": to_
                }
            )

            self.assertEqual(res.status_code, status.HTTP_200_OK)

            res_data = paginated_data_or_not(res)
            exp_data = self.woman_util.filter_by_field_range(
                from_=from_, to_=to_, field=field
            )

            self.assertEqual(res_data, exp_data)

    def test_choice_type_field_filters(self):
        """
        Test Woman page  filters to choice type fields
        like "hair", "eye" which need from_{} and to_{}
        in query parameters
        """
        choices_field = ["hair", "eye"]
        model = Model.objects.filter(gender="woman").last()

        for field in choices_field:
            # get model parameter
            model_param = getattr(model, field)

            res = self.client.get(
                MAN_LIST_PAGE_URL,
                {f"{field}": model_param}
            )

            self.assertEqual(res.status_code, status.HTTP_200_OK)

            res_data = paginated_data_or_not(res)
            exp_data = self.woman_util.filter_by_choice_field(
                field=field, value=model_param
            )

            self.assertEqual(res_data, exp_data)

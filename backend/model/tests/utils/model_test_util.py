"""Utils for testing model app"""
from django.urls import reverse

from ...models import Model
from ...serializers import (
    ModelSerializer,
    WomanModelListSerializer,
    ManModelListSerializer
)


def model_detail_url(model_id: int, gender: str = "main"):
    """Returns URL for Detail pages on Main, Man, Woman list models pages"""
    return reverse(f"model:{gender}-detail", args=[model_id])


def paginated_data_or_not(data):
    """
    If paginated return data from ['result']
    else return data
    """
    if "results" in data:
        return data["results"]
    return data


class UtilFilterSearchSerialize:
    """
    Main, Man and Woman page has a lot of common
    functionality like searching, or man and woman
    pages share same filters.
    And all models are using one serializer for response
    So need to duplicate
    """

    def __init__(
            self,
            limit: int,
            offset: int,
            gender: str = None
    ):

        self.limit = limit
        self.offset = offset
        self.gender = gender
        self.queryset = (
            Model.objects.filter(gender=gender)
            if gender else Model.objects.all()
        )

    def get_serializer(self):
        if self.gender == "man":
            return ManModelListSerializer
        elif self.gender == "woman":
            return WomanModelListSerializer
        return ModelSerializer

    def serializing_list_of_searched_models(
            self, search: str, request=None
    ) -> [dict]:
        """
        Serialize list of models including pagination values
        and include search query parameters
        By default serialize first page

        :param str search: The search query string
        :param request: is test request from APIClient
        :rtype list[dict]
        """
        exp_data = Model.objects.filter(
            model_user__full_name__icontains=search
        )
        return self.serializing_list_of_models(
            data=exp_data, request=request
        )

    def serializing_list_of_models(
            self, request=None,  data: list = None
    ) -> [dict]:
        """
        Serialize list of models including pagination values
        By default serialize firs page

        :param list data: List of data to just serialize
        :param request: is test request from APIClient
        :return: A list of serialized model dictionaries
        :rtype list[dict]
        """
        exp_data = (
            data[self.offset: self.limit + self.offset] if data
            else self.queryset.all()[self.offset: self.limit + self.offset]
        )
        serializer = self.get_serializer()(
            exp_data, many=True, context={"request": request}
        )

        return serializer.data

    def filter_by_field_range(
            self, field: str, from_: int, to_: int, request=None
    ):
        """
        Filters Model base on range parameters like
        height, bust, waist, hips
        :param field: str
        :param from_: int
        :param to_: int
        :param request: is test request from APIClient
        :return: list[dict]
        """
        filter_kwg = {
            f"{field}__gte": from_,
            f"{field}__lte": to_,
        }
        exp_data = self.queryset.filter(**filter_kwg)

        return self.serializing_list_of_models(
            data=exp_data, request=request
        )

    def filter_by_choice_field(
            self, field: str, value: str, request=None
    ):
        """
        Filter Model by choices field like hair and eye color,
        pass choice type field and color to filter models
        :param field: str
        :param value: str
        :param request: is test request from APIClient
        :return: list[dict]
        """
        filter_kwg = {f"{field}": value}
        exp_data = self.queryset.filter(**filter_kwg)

        return self.serializing_list_of_models(
            data=exp_data, request=request
        )

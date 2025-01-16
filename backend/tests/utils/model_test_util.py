"""Utils for testing model app"""
from backend.model.models import Model
from backend.model.serializers import (
    ModelListSerializer
)


def paginated_data_or_not(data):
    """
    If paginated return data from ['result']
    else return data
    """
    if "results" in data:
        return data["results"]
    return data


class UtilSerializingModels:
    def __init__(
            self,
            limit: int,
            offset: int,
    ):
        """
        Parameters for pagination
        :param int limit: Number of results to return
        :param int offset: (Optional) Starting index of the result
        """
        self.limit = limit
        self.offset = offset

    def serializing_list_of_searched_models(
            self, search: str
    ) -> [dict]:
        """
        Serialize list of models including pagination values
        and include search query parameters
        By default serialize first page

        :param str search: The search query string
        :rtype list[dict]
        """
        exp_data = Model.objects.filter(
            model_user__first_name__icontains=search
        )
        return self.serializing_list_of_models(
            data=exp_data
        )

    def serializing_list_of_models(
            self, data: list = None
    ) -> [dict]:
        """
        Serialize list of models including pagination values
        By default serialize firs page

        :param list data: List of data to just serialize
        :return: A list of serialized model dictionaries
        :rtype list[dict]
        """
        exp_data = (
            data[self.limit: self.offset] if data
            else Model.objects.all()[self.limit: self.offset]
        )
        serializer = ModelListSerializer(exp_data, many=True)

        return serializer.data


class UtilFilterSearchSerialize(UtilSerializingModels):
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

        super().__init__(limit=limit, offset=offset)
        self.queryset = (
            Model.objects.filter(gender=gender)
            if gender else Model.objects.all()
        )

    def filter_by_field_range(self, field: str, from_: int, to_: int):
        """
        Filters Model base on range parameters like
        height, bust, waist, hips
        :param field: str
        :param from_: int
        :param to_: int
        :return: list[dict]
        """
        filter_kwg = {
            f"{field}__qte": from_,
            f"{field}__lte": to_,
        }
        exp_data = self.queryset.filter(**filter_kwg)

        return self.serializing_list_of_models(data=exp_data)

    def filter_by_choice_field(self, field: str, value: str):
        """
        Filter Model by choices field like hair and eye color,
        pass choice type field and color to filter models
        :param field: str
        :param value: str
        :return: list[dict]
        """
        filter_kwg = {f"{field}": value}
        exp_data = self.queryset.filter(**filter_kwg)

        return self.serializing_list_of_models(data=exp_data)

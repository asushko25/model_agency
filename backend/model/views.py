from django.db.models import Q
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import Model
from .serializers import ModelListSerializer


def filter_models(queryset, params):
    height_min = params.get("height_min")
    height_max = params.get("height_max")
    bust_min = params.get("bust_min")
    bust_max = params.get("bust_max")
    hips_min = params.get("hips_min")
    hips_max = params.get("hips_max")
    waist_min = params.get("waist_min")
    waist_max = params.get("waist_max")
    hair = params.get("hair")
    eye_color = params.get("eye_color")

    if height_min:
        queryset = queryset.filter(height__gte=height_min)
    if height_max:
        queryset = queryset.filter(height__lte=height_max)
    if bust_min:
        queryset = queryset.filter(bust__gte=bust_min)
    if bust_max:
        queryset = queryset.filter(bust__lte=bust_max)
    if hips_min:
        queryset = queryset.filter(hips__gte=hips_min)
    if hips_max:
        queryset = queryset.filter(hips__lte=hips_max)
    if waist_min:
        queryset = queryset.filter(waist__gte=waist_min)
    if waist_max:
        queryset = queryset.filter(waist__lte=waist_max)
    if hair:
        queryset = queryset.filter(hair=hair)
    if eye_color:
        queryset = queryset.filter(eye_color=eye_color)

    return queryset


class FilterSearchMixin:
    @staticmethod
    def apply_filters(queryset, params):
        """Apply filters to the queryset based on parameters"""
        filter_field = {
            "height__gte": params.get("height_min"),
            "height__lte": params.get("height_max"),
            "bust__gte": params.get("bust_min"),
            "bust__lte": params.get("bust_max"),
            "hips__gte": params.get("hips_min"),
            "hips__lte": params.get("hips_max"),
            "waist__gte": params.get("waist_min"),
            "waist__lte": params.get("waist_max"),
            "hair": params.get("hair"),
            "eye_color": params.get("eye_color"),
        }

        for field, value in filter_field.items():
            if value:
                queryset = queryset.filter(**{field: value})

        return queryset

    @staticmethod
    def search_by_full_name(queryset, full_name):
        """Search list of model base on model `full_name` field"""
        if full_name:
            queryset = queryset.filter(
                model_user__full_name__icontains=full_name
            )

        return queryset


class MainViewSet(
    FilterSearchMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Model.objects.all()
    serializer_class = ModelListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get("search", "").strip()

        return self.search_by_full_name(queryset, search_query)


class ManModelViewSet(
    FilterSearchMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Model.objects.filter(gender="man")
    serializer_class = ModelListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.apply_filters(queryset, self.request.query_params)
        search_query = self.request.query_params.get("search", "").strip()

        return self.search_by_full_name(queryset, search_query)


class WomanModelViewSet(
    FilterSearchMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Model.objects.filter(gender="woman")
    serializer_class = ModelListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.apply_filters(queryset, self.request.query_params)
        search_query = self.request.query_params.get("search", "").strip()

        return self.search_by_full_name(queryset, search_query)

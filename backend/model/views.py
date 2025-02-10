import logging

from django.core.cache import cache

from rest_framework import mixins
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import GenericViewSet

from .models import Model
from .serializers import (
    WomanModelListSerializer,
    WomanModelDetailSerializer,
    ManModelDetailSerializer,
    ManModelListSerializer,
    ModelSerializer,
    ModelDetailSerializer,
)

logger = logging.getLogger("model_app")


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

        logger.debug(f"Query Filters values {params}")

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

        logger.debug(f"Search query value {full_name}")

        return queryset


class CustomPagination(LimitOffsetPagination):
    default_limit = 6
    max_limit = 100


class MainViewSet(
    FilterSearchMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Model.objects.select_related(
        "model_user"
    ).prefetch_related("images")
    serializer_class = ModelSerializer
    pagination_class = CustomPagination
    lookup_field = "id"

    def get_queryset(self):
        # get queryset for main page from DB cache, if we do not
        # have it the set it
        queryset = cache.get_or_set(
            "main_model_queryset", super().get_queryset()
        )
        search_query = self.request.query_params.get("search", "").strip()

        return self.search_by_full_name(queryset, search_query)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ModelDetailSerializer
        return ModelSerializer


class ManModelViewSet(
    FilterSearchMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Model.objects.filter(
        gender="man"
    ).select_related(
        "model_user"
    ).prefetch_related("images")
    serializer_class = ModelSerializer
    pagination_class = CustomPagination
    lookup_field = "id"

    def get_queryset(self):
        # get queryset for man page from DB cache, if we do not
        # have it the set it
        queryset = cache.get_or_set(
            "man_model_queryset", super().get_queryset()
        )

        queryset = self.apply_filters(queryset, self.request.query_params)
        search_query = self.request.query_params.get("search", "").strip()

        return self.search_by_full_name(queryset, search_query)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ManModelDetailSerializer
        return ManModelListSerializer


class WomanModelViewSet(
    FilterSearchMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Model.objects.filter(
        gender="woman"
    ).select_related(
        "model_user"
    ).prefetch_related("images")
    serializer_class = ModelSerializer
    pagination_class = CustomPagination
    lookup_field = "id"

    def get_queryset(self):
        # get queryset for woman page from DB cache, if we do not
        # have it the set it
        queryset = cache.get_or_set(
            "woman_model_queryset", super().get_queryset()
        )

        queryset = self.apply_filters(queryset, self.request.query_params)
        search_query = self.request.query_params.get("search", "").strip()

        return self.search_by_full_name(queryset, search_query)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return WomanModelDetailSerializer
        return WomanModelListSerializer

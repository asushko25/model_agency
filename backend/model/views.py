import logging

from django.core.cache import cache

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
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

    @extend_schema(
        summary="List all models",
        description="Returns a paginated list of models",
        parameters=[
            OpenApiParameter(
                "search",
                type=OpenApiTypes.STR,
                description="Search by full name (ex. ?search=John Doe)",
            )
        ],
        responses={200: ManModelListSerializer}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


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

        queryset = self.search_by_full_name(queryset, search_query)

        return queryset

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ManModelDetailSerializer
        return ManModelListSerializer

    @extend_schema(
        summary="List all male models",
        description="Returns a paginated list of male models with optional filtering.",
        parameters=[
            OpenApiParameter(
                "search",
                type=OpenApiTypes.STR,
                description="Search by full name (ex. ?search=John Doe)",
            ),
            OpenApiParameter(
                "height_min",
                type=OpenApiTypes.INT,
                description="Minimum height (cm) (ex. ?height_min=170)",
            ),
            OpenApiParameter(
                "height_max",
                type=OpenApiTypes.INT,
                description="Maximum height (cm) (ex. ?height_max=190)",
            ),
            OpenApiParameter(
                "bust_min",
                type=OpenApiTypes.INT,
                description="Minimum bust size (cm) (ex. ?bust_min=80)",
            ),
            OpenApiParameter(
                "bust_max",
                type=OpenApiTypes.INT,
                description="Maximum bust size (cm) (ex. ?bust_max=100)",
            ),
            OpenApiParameter(
                "hips_min",
                type=OpenApiTypes.INT,
                description="Minimum hips size (cm) (ex. ?hips_min=85)",
            ),
            OpenApiParameter(
                "hips_max",
                type=OpenApiTypes.INT,
                description="Maximum hips size (cm) (ex. ?hips_max=110)",
            ),
            OpenApiParameter(
                "waist_min",
                type=OpenApiTypes.INT,
                description="Minimum waist size (cm) (ex. ?waist_min=60)",
            ),
            OpenApiParameter(
                "waist_max",
                type=OpenApiTypes.INT,
                description="Maximum waist size (cm) (ex. ?waist_max=80)",
            ),
            OpenApiParameter(
                "hair",
                type=OpenApiTypes.STR,
                description="Filter by hair color (ex. ?hair=blonde)",
            ),
            OpenApiParameter(
                "eye_color",
                type=OpenApiTypes.STR,
                description="Filter by eye color (ex. ?eye_color=blue)",
            ),
        ],
        responses={200: ManModelListSerializer}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


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

        queryset = self.search_by_full_name(queryset, search_query)

        return queryset

    def get_serializer_class(self):
        if self.action == "retrieve":
            return WomanModelDetailSerializer
        return WomanModelListSerializer

    @extend_schema(
        summary="List all female models",
        description="Returns a paginated list of female models with optional filtering.",
        parameters=[
            OpenApiParameter(
                "search",
                type=OpenApiTypes.STR,
                description="Search by full name (ex. ?search=Jane Doe)",
            ),
            OpenApiParameter(
                "height_min",
                type=OpenApiTypes.INT,
                description="Minimum height (cm) (ex. ?height_min=160)",
            ),
            OpenApiParameter(
                "height_max",
                type=OpenApiTypes.INT,
                description="Maximum height (cm) (ex. ?height_max=185)",
            ),
            OpenApiParameter(
                "bust_min",
                type=OpenApiTypes.INT,
                description="Minimum bust size (cm) (ex. ?bust_min=75)",
            ),
            OpenApiParameter(
                "bust_max",
                type=OpenApiTypes.INT,
                description="Maximum bust size (cm) (ex. ?bust_max=100)",
            ),
            OpenApiParameter(
                "hips_min",
                type=OpenApiTypes.INT,
                description="Minimum hips size (cm) (ex. ?hips_min=85)",
            ),
            OpenApiParameter(
                "hips_max",
                type=OpenApiTypes.INT,
                description="Maximum hips size (cm) (ex. ?hips_max=115)",
            ),
            OpenApiParameter(
                "waist_min",
                type=OpenApiTypes.INT,
                description="Minimum waist size (cm) (ex. ?waist_min=55)",
            ),
            OpenApiParameter(
                "waist_max",
                type=OpenApiTypes.INT,
                description="Maximum waist size (cm) (ex. ?waist_max=75)",
            ),
            OpenApiParameter(
                "hair",
                type=OpenApiTypes.STR,
                description="Filter by hair color (ex. ?hair=black)",
            ),
            OpenApiParameter(
                "eye_color",
                type=OpenApiTypes.STR,
                description="Filter by eye color (ex. ?eye_color=brown)",
            ),
        ],
        responses={200: WomanModelListSerializer}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

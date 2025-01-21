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


def search_by_name(queryset, search_query):
    if search_query:
        queryset = queryset.filter(
            Q(model_user__first_name__icontains=search_query)
            | Q(model_user__last_name__icontains=search_query)
        )
    return queryset


class MainViewSet(
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Model.objects.all()
    serializer_class = ModelListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = filter_models(queryset, self.request.query_params)
        search_query = self.request.query_params.get("search", "").strip()
    
        if search_query:
            queryset = search_by_name(queryset, search_query)
    
        return queryset


class ManModelViewSet(
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Model.objects.filter(gender="man")
    serializer_class = ModelListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = filter_models(queryset, self.request.query_params)
        search_query = self.request.query_params.get("search", "").strip()
    
        if search_query:
            queryset = search_by_name(queryset, search_query)
    
        return queryset


class WomanModelViewSet(
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Model.objects.filter(gender="woman")
    serializer_class = ModelListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = filter_models(queryset, self.request.query_params)
        search_query = self.request.query_params.get("search", "").strip()

        if search_query:
            queryset = search_by_name(queryset, search_query)

        return queryset

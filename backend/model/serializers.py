from rest_framework import serializers
from django.conf import settings

from .models import Model, ModelImages


class ModelImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelImages
        fields = ["image", "caption"]


class ModelSerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(
        view_name="model:main-detail", lookup_field="id"
    )
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Model
        fields = [
            "id",
            "full_name",
            "city",
            "country",
            "image_url",
            "detail_url"
        ]

    def get_image_url(self, obj):
        # query first() is not optimized for prefetch reverse relationships
        # making N + 1 issues, that why we are not using it
        first_image = next(iter(obj.images.all()), None)
        if first_image and first_image.image:
            if settings.DEBUG:  # Development: Use full URL
                request = self.context["request"]
                return request.build_absolute_uri(first_image.image.url)
            else:  # Production: Serve directly from Cloudflare (MEDIA_URL)
                return first_image.image.url
        return None


class ModelDetailSerializer(serializers.ModelSerializer):
    images = ModelImagesSerializer(many=True, read_only=True)
    contact_url = serializers.HyperlinkedIdentityField(
        view_name="contact:contact-with-model", lookup_field="id"
    )

    class Meta:
        model = Model
        fields = [
            "id",
            "hair",
            "eye_color",
            "bust",
            "waist",
            "hips",
            "height",
            "images",
            "contact_url",
        ]


class WomanModelListSerializer(ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(
        view_name="model:women-detail", lookup_field="id"
    )

    class Meta:
        model = Model
        fields = [
            "id",
            "full_name",
            "city",
            "country",
            "image_url",
            "detail_url"
        ]


class WomanModelDetailSerializer(ModelDetailSerializer):

    class Meta:
        model = Model
        fields = [
            "id",
            "hair",
            "eye_color",
            "bust",
            "waist",
            "hips",
            "images",
            "contact_url",
        ]


class ManModelListSerializer(ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(
        view_name="model:men-detail", lookup_field="id"
    )

    class Meta:
        model = Model
        fields = [
            "id",
            "full_name",
            "city",
            "country",
            "image_url",
            "detail_url"
        ]


class ManModelDetailSerializer(ModelDetailSerializer):

    class Meta:
        model = Model
        fields = [
            "id",
            "hair",
            "eye_color",
            "bust",
            "waist",
            "hips",
            "images",
            "contact_url",
        ]

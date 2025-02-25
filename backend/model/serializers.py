from rest_framework import serializers

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
        return (
            first_image.image.url if first_image and first_image.image
            else None
        )


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

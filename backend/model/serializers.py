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
    photo = serializers.SerializerMethodField()

    class Meta:
        model = Model
        fields = ["id", "full_name", "city", "country", "photo", "detail_url"]

    def get_photo(self, obj):
        first_image = obj.images.first()
        if first_image and first_image.image:
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
            "images",
            "contact_url",
        ]


class WomanModelListSerializer(ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(
        view_name="model:woman-detail", lookup_field="id"
    )

    class Meta:
        model = Model
        fields = ["id", "full_name", "city", "country", "photo", "detail_url"]


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
        view_name="model:man-detail", lookup_field="id"
    )

    class Meta:
        model = Model
        fields = ["id", "full_name", "city", "country", "photo", "detail_url"]


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

from rest_framework import serializers

from .models import Model, ModelImages


class ModelImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelImages
        fields = ["image", "caption"]


class ModelSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(source="images.first.image")

    class Meta:
        model = Model
        fields = ["id", "full_name", "city", "country", "photo"]


class ModelDetailSerializer(serializers.ModelSerializer):
    images = ModelImagesSerializer(many=True, read_only=True)
    contact_url = serializers.HyperlinkedIdentityField(
        view_name="contact:contact-with-model", lookup_field="id"
    )

    class Meta:
        model = Model
        fields = ["id", "hair", "eye_color", "bust", "waist", "hips", "images", "contact_url"]


class WomanModelListSerializer(ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(
        view_name="model:woman-detail", lookup_field="id"
    )

    class Meta:
        model = Model
        fields = ["full_name", "city", "country", "photo", "detail_url"]


class WomanModelDetailSerializer(ModelDetailSerializer):

    class Meta:
        model = Model
        fields = [
            "hair",
            "eye_color",
            "bust",
            "waist",
            "hips",
            "images",
            "contact_url"
        ]


class ManModelListSerializer(ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(
        view_name="model:man-detail", lookup_field="id"
    )

    class Meta:
        model = Model
        fields = ["full_name", "city", "country", "photo", "detail_url"]


class ManModelDetailSerializer(ModelDetailSerializer):


    class Meta:
        model = Model
        fields = [
            "hair",
            "eye_color",
            "bust",
            "waist",
            "hips",
            "images",
            "contact_url",
        ]

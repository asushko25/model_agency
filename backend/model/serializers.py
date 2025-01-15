from rest_framework import serializers

from .models import Model, ModelImages


class ModelImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelImages
        fields = ["image", "caption"]


class ModelListSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(source="images.first.image")

    class Meta:
        model = Model
        fields = ["id", "full_name", "city", "country", "photo"]


class ModelDetailSerializer(serializers.ModelSerializer):
    images = ModelImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Model
        fields = [
            "hair",
            "eye_color",
            "bust",
            "waist",
            "hips",
            "images"
        ]

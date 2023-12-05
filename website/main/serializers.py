from rest_framework import serializers
from .models import UserModel, AdvertModel, ImageModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = 'all'


class AdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertModel
        fields = 'all'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ('id', 'name', 'image', 'advert')
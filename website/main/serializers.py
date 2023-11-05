from rest_framework import serializers
from .models import UserModel, AdvertModel, ImageModel


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = 'all'


class AdvertModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertModel
        fields = 'all'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ('id', 'name', 'image')
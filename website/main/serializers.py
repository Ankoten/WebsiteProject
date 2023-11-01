from rest_framework import serializers
from .models import UserModel, AdvertModel


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = 'all'


class AdvertModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertModel
        fields = 'all'

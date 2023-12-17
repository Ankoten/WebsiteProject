from django.contrib.auth import get_user_model , authenticate
from rest_framework import serializers
from .models import Advert, Category, User

UserModel = get_user_model()

class AdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

    def create(self, clean_data):
        user_obj = User.objects.create_user(
            username=clean_data['username'],
            email=clean_data['email'],
            password=clean_data['password']
        )
        user_obj.save()
        return user_obj


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def check_user(self, clean_data):
        user = authenticate(
            username=clean_data['username'],
            password=clean_data['password']
        )
        if not user:
            raise serializers.ValidationError("Такого пользователя не существует")
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('email', 'name')
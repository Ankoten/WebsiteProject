from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from website.main.models import UserModel, AdvertModel
from rest_framework import viewsets
from website.main.serializers import UserModelSerializer, AdvertModelSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer


def get_user(request, user_id):
    user = UserModel.objects.get(id=user_id)
    user_sr = UserModelSerializer(user)
    return Response({'post': user_sr})
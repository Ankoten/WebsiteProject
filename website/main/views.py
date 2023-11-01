from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserModel, AdvertModel

from .serializers import UserModelSerializer, AdvertModelSerializer


class UserInfoView(APIView):
    def get (self, request):
        users = UserModel.objects.all()
        return Response({'post': UserModelSerializer(users, many=True).data})


class UserInfoView(APIView):
    def get (self, request):
        advert = AdvertModel.objects.all()
        return Response({'post': AdvertModelSerializer(advert, many=True).data})

#def index(request):
    #return Response("<h4>Проверка<h4>")

#def registration(request):
    #return Response("<h4>Регистрация<h4>")
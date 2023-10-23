from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import viewsets
from .serializers import YourModelSerializer


class YourModelViewSet(viewsets.ModelViewSet):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer

class UserInfoView(APIView):
    def get (self, request):
        return Response({'name': 'John', 'surname': 'Jackson', 'age': 21})

#def index(request):
    #return Response("<h4>Проверка<h4>")

#def registration(request):
    #return Response("<h4>Регистрация<h4>")
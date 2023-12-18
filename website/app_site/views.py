from django.contrib.auth import logout, login
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Advert, Category, User
from rest_framework import status, viewsets, permissions
from .serializers import AdvertSerializer, CategorySerializer, UserSerializer, UserRegistrationSerializer, \
    UserLoginSerializer
from .validations import custom_validation, validate_username, validate_password


@api_view(['GET', 'PUT', 'DELETE'])
def AdvertModel_detail(request, pk):

    try:
        advertM = Advert.objects.get(pk=pk)
    except Advert.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AdvertSerializer(advertM)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AdvertSerializer(advertM, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        advertM.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Advertview(APIView):
    def get (self,request):
        queryset = Advert.objects.all()
        serializer = AdvertSerializer(queryset, many = True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

class Categoriesview(APIView):
    def get (self,request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many = True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class UserModelView(APIView):
    def get (self, request):
        users = User.objects.all()
        return Response({'post': UserSerializer(users, many=True).data})

class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        try:
            clean_data = custom_validation(request.data)
            serializer = UserRegistrationSerializer(data=clean_data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.create(clean_data)
                if user:
                    login(request, user)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        data = request.data
        assert validate_username(data)
        assert validate_password(data)
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogout(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class UserView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)
    def get(self, request):
        if request.user.is_authenticated:
            serializer = UserSerializer(request.user)
            return Response({'user': serializer.data}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)

class SaleAdCreateDeleteView(APIView):
    def post(self, request):
        serializer = AdvertSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            sale_ad =Advert.objects.get(pk=pk)
            sale_ad.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Advert.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)




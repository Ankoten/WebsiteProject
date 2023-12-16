from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import UserModel, AdvertModel, ImageModel
from rest_framework import viewsets, status
from django.views.generic import View
from PIL import Image
from .serializers import UserSerializer, AdvertSerializer, ImageSerializer

@api_view(['GET', 'PUT', 'DELETE'])
def AdvertModel_detail(request, pk):

    try:
        advertM = AdvertModel.objects.get(pk=pk)
    except AdvertModel.DoesNotExist:
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




class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
class UserModelView(APIView):
    def get (self, request):
        users = UserModel.objects.all()
        return Response({'post': UserModelSerializer(users, many=True).data})

class AdvertViewSet(viewsets.ModelViewSet):
    queryset = AdvertModel.objects.all()
    serializer_class = AdvertSerializer
class AdvertInfoView(APIView):
    def get (self, request):
        advert = AdvertModel.objects.all()
        return Response({'post': AdvertModelSerializer(advert, many=True).data})



class ImageViewSet(viewsets.ModelViewSet):
        queryset = ImageModel.objects.all()
        serializer_class = ImageSerializer
class ImageView(View):
    def get(self, request, *args, **kwargs):
        image_id = kwargs.get('image_id')
        image = ImageModel.objects.get(id=image_id)
        response = HttpResponse()
        response['Content-Type'] = 'image/jpeg'
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(image.name)
        response.write(image.image.read())
        return response


def get_image(request, image_id):
    # Получаем объект модели ImageModel по его ID
    image = ImageModel.objects.get(id=image_id)
    # Открываем изображение с помощью PIL
    pil_image = ImageModel.open(image.image.path)
    # Конвертируем изображение в формат JPEG
    jpeg_image = pil_image.convert('RGB')
    # Создаем HTTP-ответ с содержимым изображения в формате JPEG
    response = HttpResponse(content_type='image/jpeg')
    jpeg_image.save(response, 'JPEG')

    return response

def get_image_advert(request, advert):
    # Получаем объект модели ImageModel по его ID
    image = ImageModel.objects.get(adver_id=advert)
    # Открываем изображение с помощью PIL
    pil_image = ImageModel.open(image.image.path)
    # Конвертируем изображение в формат JPEG
    jpeg_image = pil_image.convert('RGB')
    # Создаем HTTP-ответ с содержимым изображения в формате JPEG
    response = HttpResponse(content_type='image/jpeg')
    jpeg_image.save(response, 'JPEG')

    return response
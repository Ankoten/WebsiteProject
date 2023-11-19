from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserModel, AdvertModel, ImageModel
from rest_framework import viewsets
from django.views.generic import View
from PIL import Image
from .serializers import UserModelSerializer, AdvertModelSerializer, ImageSerializer


class UserModelView(APIView):
    def get (self, request):
        users = UserModel.objects.all()
        return Response({'post': UserModelSerializer(users, many=True).data})


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

def get_image_advert(request, advert_id):
    # Получаем объект модели ImageModel по его ID
    image = ImageModel.objects.get(advert=advert_id)
    # Открываем изображение с помощью PIL
    pil_image = ImageModel.open(image.image.path)
    # Конвертируем изображение в формат JPEG
    jpeg_image = pil_image.convert('RGB')
    # Создаем HTTP-ответ с содержимым изображения в формате JPEG
    response = HttpResponse(content_type='image/jpeg')
    jpeg_image.save(response, 'JPEG')

    return response
from . import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ImageViewSet
from .views import ImageView
from .views import get_image
router = DefaultRouter()
#router.register(r'yourmodel', UserModelViewSet)
router.register(r'images', ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('registration', UserModelViewSet.as_view({'post':'create'}), name='registration')
    path('images/<int:image_id>/', ImageView.as_view(), name='image'),
    path('api/get_image/<int:image_id>/', get_image, name='get_image'),
]

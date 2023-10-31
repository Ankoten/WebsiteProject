from . import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserModelViewSet

router = DefaultRouter()
router.register(r'yourmodel', UserModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('registration', UserModelViewSet.as_view({'post':'create'}), name='registration')
]

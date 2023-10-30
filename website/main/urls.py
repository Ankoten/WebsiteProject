from . import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import YourModelViewSet

router = DefaultRouter()
router.register(r'yourmodel', YourModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('registration', YourModelViewSet.as_view({'post': 'create'}), name='registration')
]

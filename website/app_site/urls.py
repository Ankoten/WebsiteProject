from . import views
from django.urls import path
from .views import ImageView
from .views import get_image

urlpatterns = [
    path('', views.HouseList.as_view(), name='main'),
    #path('', include(router.urls)),
    path('images/<int:image_id>/', ImageView.as_view(), name='image'),
    path('api/get_image/<int:image_id>/', get_image, name='get_image'),
    path('', views.HouseList.as_view(), name='main'),
    path('realty/myadv/', views.MyHouseList.as_view(), name='my_house'),
    path('realty/<int:pk>/', views.HouseDetail.as_view(), name='house_detail'),
    path('realty/<int:pk>/edit/', views.HouseEdit.as_view(), name='house_edit'),
    path('realty/<int:pk>/delete/', views.HouseDelete.as_view(), name='house_delete'),
    path('realty/add/', views.HouseCreate.as_view(), name='house_create'),
    path('realty/foto/<int:pk>/delete/', views.HouseFotoDelete.as_view(), name='delete_foto'),
]


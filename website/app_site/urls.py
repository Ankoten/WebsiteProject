
from django.urls import path
from .views import Advertview, Categoriesview, SaleAdCreateDeleteView
from . import views



urlpatterns = [
    path("categories/", Categoriesview.as_view()),
    path('Advert/',Advertview.as_view()),
    path('sale-ads/', SaleAdCreateDeleteView.as_view(), name='sale-ad-create-delete'),
    path('sale-ads/<int:pk>/', SaleAdCreateDeleteView.as_view(), name='sale-ad-delete'),
    path('register', views.UserRegister.as_view(), name='Регистрация'),
    path('login', views.UserLogin.as_view(), name='Войти'),
    path('logout', views.UserLogout.as_view(), name='Выйти'),
    path('user', views.UserView.as_view(), name='Пользователь'),
]


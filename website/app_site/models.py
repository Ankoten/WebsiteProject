from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class Category(models.Model):
    title = models.CharField(max_length=30, verbose_name='Тип жилья')
    class Meta:
        verbose_name = 'Тип жилья'
        verbose_name_plural = 'Типы жилья'

    def __str__(self):
        return f'Тип жилья: {self.title}'

class Advert(models.Model):
    advert = models.CharField(max_length=100, null=False)
    price = models.PositiveBigIntegerField(null=False)
    address = models.CharField(max_length=1000, null=False)
    rooms = models.PositiveSmallIntegerField(null=False)
    description = models.TextField()
    payment_hcs = models.BooleanField(default=False)
    deposit = models.PositiveBigIntegerField(default=0, null=False)
    total_area = models.FloatField(max_length=1000, null=False)
    kitchen_area = models.FloatField(max_length=100, null=False)
    living_area = models.FloatField(max_length=100, null=False)
    price_per_meter = models.PositiveBigIntegerField(null=False)
    ceiling_hight = models.FloatField(max_length=1000, null=False)
    the_method_of_sale = models.CharField(max_length=1000, null=False)
    floor = models.PositiveSmallIntegerField(null=False)
    prepayment = models.PositiveSmallIntegerField(null=False)
    the_rental_period = models.CharField(max_length=100, null=False)
    living_conditions = models.CharField(max_length=100, null=False)
    title = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Жилье'
        verbose_name_plural = 'Жилье'
    def __str__(self):
        return f'{self.advert} ({self.price})'


class AppUserManager(BaseUserManager):
    def create_user(self, name, email, telephone, surname, password=None):
        if not name:
            raise ValueError('Необходимо указать имя ')
        if not surname:
            raise ValueError('Необходимо указать фамилию ')
        if not email:
            raise ValueError('Необходимо указать почту')
        if not password:
            raise ValueError('Необходимо указать пароль')
        if not telephone:
            raise ValueError('Необходимо указать телефон')
        email = self.normalize_email(email)
        user = self.model(username=name, surname=surname, telephone=telephone, email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, name, email, password=None):
        user = self.create_user(name, email, password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    groups = models.ManyToManyField('auth.Group', related_name='app_users_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='app_users_permissions')
    username = models.CharField(max_length=50, unique=True, default=False)
    surname = models.CharField(max_length=100, verbose_name='Фамилия', null=True)
    telephone = models.CharField(max_length=16, verbose_name='Телефон', blank=True)
    email = models.EmailField(max_length=50, default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = AppUserManager()

    def __str__(self):
        return self.username




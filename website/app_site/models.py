from django.contrib.auth.models import User
from django.db import models
from pathlib import Path
from django.urls import reverse
#class UserModel(models.Model):
    #name = models.CharField(max_length=100, null=False)
    #surname = models.CharField(max_length=100, null=False)
    #telephone = models.CharField(max_length=16, verbose_name='Телефон', blank=True)
    #password = models.CharField(max_length=100, null=False)

    #def str(self):
        #return {self.name, self.surname}

class AdvertModel(models.Model):
    advert = models.CharField(max_length=100, null=False)
    price = models.PositiveBigIntegerField(null=False)
    address = models.CharField(max_length=1000, null=False)
    rooms = models.PositiveSmallIntegerField(null=False)
    description = models.TextField()
    payment_hcs = models.BooleanField(default=False)
    deposit = models.PositiveBigIntegerField(default=0, null=False)
    #user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
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

    class Meta:
        verbose_name = 'Жилье'
        verbose_name_plural = 'Жилье'
    def str(self):
        return self.advert

class ImageModel(models.Model):
    name = models.CharField(max_length=255,default='default_name' )
    image = models.ImageField(upload_to='images/',default= 'default_image.jpg')
    advert = models.ForeignKey(AdvertModel, on_delete=models.CASCADE, default = 0)


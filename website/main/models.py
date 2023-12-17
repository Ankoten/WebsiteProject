from django.db import models

class UserModel(models.Model):
    name = models.CharField(max_length=100, null=False)
    surname = models.CharField(max_length=100, null=False)
    telephone = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=100, null=False)

    def str(self):
        return {self.name, self.surname}

class AdvertModel(models.Model):
    advert = models.CharField(max_length=100, null=False)
    price = models.PositiveBigIntegerField(null=False)
    address = models.CharField(max_length=1000, null=False)
    rooms = models.PositiveSmallIntegerField(null=False)
    description = models.TextField()
    payment_hcs = models.BooleanField(default=False)
    deposit = models.PositiveBigIntegerField(default=0, null=False)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    total_area = models.FloatField(max_length=1000, null=False, default=0)
    kitchen_area = models.FloatField(max_length=100, null=False, default=0)
    living_area = models.FloatField(max_length=100, null=False, default=0)
    price_per_meter = models.PositiveBigIntegerField(null=False, default=0)
    ceiling_hight = models.FloatField(max_length=1000, null=False, default=0)
    the_method_of_sale = models.CharField(max_length=1000, null=False, default='null')
    floor = models.PositiveSmallIntegerField(null=False, default=0)
    prepayment = models.PositiveSmallIntegerField(null=False, default=0)
    the_rental_period = models.CharField(max_length=100, null=False, default='null')
    living_conditions = models.CharField(max_length=100, null=False, default='null')
    def str(self):
        return self.advert

class ImageModel(models.Model):
    name = models.CharField(max_length=255,default='default_name' )
    image = models.ImageField(upload_to='images/',default= 'default_image.jpg')
    advert = models.ForeignKey(AdvertModel, on_delete=models.CASCADE, default=0)

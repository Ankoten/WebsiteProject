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
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    def str(self):
        return self.advert

class ImageModel(models.Model):
    name = models.CharField(max_length=255,default='default_name' )
    image = models.ImageField(upload_to='images/',default= 'default_image.jpg')
    advert = models.ForeignKey(AdvertModel, on_delete=models.CASCADE)

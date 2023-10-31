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
    image = models.CharField(max_length=100, null=False)
    description = models.TextField()
    uuser = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    def str(self):
        return self.advert
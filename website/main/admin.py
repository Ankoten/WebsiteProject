from django.contrib import admin
from .models import UserModel, AdvertModel, ImageModel
# Register your models here.
admin.site.register(UserModel)
admin.site.register(AdvertModel)
admin.site.register(ImageModel)
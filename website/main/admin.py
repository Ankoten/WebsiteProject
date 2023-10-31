from django.contrib import admin
from .models import UserModel, AdvertModel
# Register your models here.
admin.site.register(UserModel)
admin.site.register(AdvertModel)
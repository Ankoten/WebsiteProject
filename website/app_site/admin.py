from django.contrib import admin
from .models import Advert, User, Category, AppUser

admin.site.register(Advert)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(AppUser)
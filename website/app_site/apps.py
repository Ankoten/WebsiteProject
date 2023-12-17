from django.apps import AppConfig

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_site'
    verbose_name = 'Квартиры'

class UserApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_api'
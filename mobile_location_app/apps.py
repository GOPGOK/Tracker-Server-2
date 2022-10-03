from django.apps import AppConfig


# конфигурация приложения
class MobileLocationAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mobile_location_app'
    # название приложения
    verbose_name = "Приложение c локациями мобильного устройства"

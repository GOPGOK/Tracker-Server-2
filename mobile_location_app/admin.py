from django.contrib import admin
from .models import Location

# надпись в шапке сайта
admin.site.site_header = 'Управление приложением c локациями мобильного устройства'

# регистрация объекта местоположения в в админ панели
admin.site.register(Location)

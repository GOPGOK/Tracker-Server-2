from django.urls import path, include

from . import views
from rest_framework import routers

# регистрируем путь к API locations в маршрутизаторе router из библиотеки rest_framework
router = routers.DefaultRouter()
router.register('locations', views.LocationViewSet)

# задаем url шаблоны приложения
urlpatterns = [
    # базовый url шаблон домашней страницы (перенаправляет на админку)
    path('', views.home, name='home'),
    # url шаблон для доступа к API
    path('api/', include(router.urls)),
]
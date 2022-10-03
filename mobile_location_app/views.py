from django.http import HttpResponseRedirect
from rest_framework import viewsets
from .serializers import *


# домашнее представление перенаправляет на страницу администрирования
def home(request):
    return HttpResponseRedirect("/admin/")


# ViewSet для локации в API, служит для получения POST запросов с местоположением от мобильного приложения
class LocationViewSet(viewsets.ModelViewSet):
    # разрешенные методы только POST
    http_method_names = ['post']
    # в качестве данных для запросов используются объекты класса Location
    queryset = Location.objects.all()

    serializer_class = LocationSerializer

    # функция для получения набора запросов
    def get_queryset(self):
        queryset = self.queryset
        return queryset

    # функция вызываемая при создании объекта
    def perform_create(self, serializer):
        # позволяет вызвать функцию save сериалазйзера для сохрания полученных данных json как объекта Location
        serializer.save()

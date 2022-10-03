from django.db import models
from django.utils.timezone import now
from django.utils import timezone


# класс объект местоположения с широтой, долготой и временем добапвления на сервер
class Location(models.Model):
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")
    datetime = models.DateTimeField(verbose_name="Дата и время получения", default=now)

    # для обращения к объектам класса
    objects = models.Manager()

    # метод для вывода данных о объектах класса в виде строки
    def __str__(self):
        local_datetime = timezone.localtime(self.datetime)
        return local_datetime.strftime('%d.%m.%Y %H:%M:%S')

    # метаинформация задает названия отображения и порядок сортировки (наиболее новые местоположения будут наверху)
    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'
        ordering = ["-datetime"]

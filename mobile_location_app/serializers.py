from rest_framework import serializers

from .models import Location


# класс позволяющий преобразовать объект класса Location в объект JSON
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        # в качестве класса модели используется класс Location
        model = Location
        # поля: id, широта, долгота, время добавления
        fields = ('id', 'latitude', 'longitude', 'datetime')
        # данные заносятся через POST только в широту и долготу,
        # id и время выставляются автоматически (поэтому readonly)
        read_only_fields = ('id', 'datetime')

    def create(self, validated_data):
        # создание объекта Location
        # данные заносятся через пост только в широту и долготу,
        # id и время выставляются автоматически
        location = Location.objects.create(
            latitude=validated_data['latitude'],
            longitude=validated_data['longitude']
        )
        # сохранение объекта в БД
        location.save()
        # возврат созданного объекта
        return location

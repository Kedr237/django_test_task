from django.db import models


class TimeSampleMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Building(TimeSampleMixin):
    city = models.CharField(max_length=255,
                            verbose_name='Город')
    street = models.CharField(max_length=255,
                              verbose_name='Улица')
    number = models.CharField(max_length=255,
                              verbose_name='Номер дома')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['city', 'street', 'number'],
                                    name='unique_city_street_number'),
        ]

    def __str__(self):
        return f'{self.city}, {self.street}, {self.number}'


class Apartment(TimeSampleMixin):
    building = models.ForeignKey(Building,
                                 on_delete=models.CASCADE,
                                 verbose_name='Адрес')
    number = models.PositiveIntegerField(verbose_name='Номер квартиры')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['building', 'number'],
                                    name='unique_building_number')
        ]

    def __str__(self):
        return f'{self.building}, {self.number}'


class Tariff(TimeSampleMixin):
    name = models.CharField(max_length=255,
                            unique=True,
                            verbose_name='Название тарифа')
    price = models.FloatField(verbose_name='Цена за кубометр')

    def __str__(self):
        return f'{self.name} : {self.price} за кубометр'


class WaterMeter(models.Model):
    apartment = models.ForeignKey(Apartment,
                                  on_delete=models.CASCADE,
                                  verbose_name='Квартира')
    tariff = models.ForeignKey(Tariff,
                               on_delete=models.CASCADE,
                               verbose_name='Название тарифа')
    value = models.IntegerField(verbose_name='Показания счетчика')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.apartment} : {self.tariff} : {self.value}'

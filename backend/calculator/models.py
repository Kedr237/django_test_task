from django.db import models
from utilities.models import Apartment


class ApartmentRent(models.Model):
    apartment = models.ForeignKey(Apartment,
                                  on_delete=models.CASCADE,
                                  verbose_name='Квартира')
    rent = models.DecimalField(max_digits=10,
                               decimal_places=2,
                               verbose_name='Квартплата')
    date_from = models.DateField(verbose_name='Дата от (включительно)')
    date_to = models.DateField(verbose_name='Дата до (не включительно)')
    created = models.DateTimeField(auto_now_add=True)

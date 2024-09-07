from decimal import Decimal

from celery import shared_task
from utilities.models import Apartment, Tariff, WaterMeter

from .models import ApartmentRent


@shared_task
def calculate_rent(building_id: int,
                   area_tariff_id: int,
                   date_from: str,
                   date_to: str):
    apartments = Apartment.objects.filter(building=building_id)
    for apartment in apartments:
        water_meters = WaterMeter.objects.filter(apartment=apartment,
                                                 created__gte=date_from,
                                                 created__lt=date_to)

        dict_wms = {}
        for wm in water_meters:
            tariff = Tariff.objects.get(id=wm.tariff.id)
            if tariff.id not in dict_wms:
                previous_wm = WaterMeter.objects.filter(apartment=apartment,
                                                        tariff=tariff,
                                                        created__lt=date_from)\
                    .order_by('-created').first()
                dict_wms[tariff.id] = {
                    'current_value': wm.value,
                    'current_date': wm.created,
                    'previous_value': previous_wm.value if previous_wm else 0,
                }
            elif dict_wms[tariff.id]['current_date'] < wm.created:
                dict_wms[tariff.id]['current_value'] = wm.value
                dict_wms[tariff.id]['current_date'] = wm.created

        area_tariff = Tariff.objects.get(id=area_tariff_id)
        total_rent = Decimal(apartment.area) * Decimal(area_tariff.price)
        for tariff_id, wm_info in dict_wms.items():
            tariff = Tariff.objects.get(id=tariff_id)
            total_rent += (Decimal(wm_info['current_value'] - Decimal(
                wm_info['previous_value']))) * Decimal(tariff.price)
        total_rent = total_rent.quantize(Decimal('0.01'))

        ApartmentRent.objects.create(
            apartment=apartment,
            rent=total_rent,
            date_from=date_from,
            date_to=date_to
        )

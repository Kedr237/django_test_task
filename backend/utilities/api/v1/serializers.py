from rest_framework import serializers
from utilities.models import Apartment, Building, Tariff, WaterMeter


class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'


class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = '__all__'


class WaterMeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterMeter
        fields = '__all__'


class BuildingInfoSerializer(serializers.ModelSerializer):
    adress = serializers.SerializerMethodField(label='Адресс')
    apartments = serializers.SerializerMethodField(label='Квартиры')

    class Meta:
        model = Building
        fields = ['adress', 'apartments']

    def get_adress(self, obj: Building):
        return f'{obj.city}, {obj.street}, {obj.number}'

    def get_apartments(self, obj: Building):
        result = []
        apartments = Apartment.objects.filter(building=obj)
        for apartment in apartments:
            result.append({
                'id': apartment.id,
                'apartment_number': apartment.number,
                'apartment_area': apartment.area,
            })
        return result

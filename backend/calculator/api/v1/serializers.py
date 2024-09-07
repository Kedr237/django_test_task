from calculator.models import ApartmentRent
from rest_framework import serializers
from utilities.models import Building, Tariff


class ApartmentRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentRent
        fields = '__all__'


class CalculateRentSerializer(serializers.Serializer):
    building_id = serializers.PrimaryKeyRelatedField(
        queryset=Building.objects.all())
    area_tariff_id = serializers.PrimaryKeyRelatedField(
        queryset=Tariff.objects.all())
    date_from = serializers.DateField(input_formats=['%d.%m.%Y'])
    date_to = serializers.DateField(input_formats=['%d.%m.%Y'])

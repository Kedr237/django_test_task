from calculator.models import ApartmentRent
from calculator.tasks import calculate_rent
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ApartmentRentSerializer, CalculateRentSerializer


class CalculateRentView(APIView):
    def post(self, request: Request):
        serializer = CalculateRentSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            calculate_rent.delay(
                building_id=data['building_id'].id,
                area_tariff_id=data['area_tariff_id'].id,
                date_from=data['date_from'],
                date_to=data['date_to'],
            )
            return Response({'status': 'Rent calculation started'},
                            status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class ApartmentRentListView(ListAPIView):
    queryset = ApartmentRent.objects.all()
    serializer_class = ApartmentRentSerializer

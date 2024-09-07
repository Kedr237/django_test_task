from django.urls import path

from .views import ApartmentRentListView, CalculateRentView

urlpatterns = [
    path('calculate-rent/', CalculateRentView.as_view()),
    path('apartments-rent/', ApartmentRentListView.as_view()),
]

from django.urls import path

from .views import add_numbers_view

urlpatterns = [
    path('add-numbers/', add_numbers_view),
]

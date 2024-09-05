from django.urls import path
from utilities.api.v1 import views

urlpatterns = [
    path('utilities/', views.MyView.as_view()),
]

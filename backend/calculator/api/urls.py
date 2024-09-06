from django.urls import include, path

urlpatterns = [
    path('v1/calculator/', include('calculator.api.v1.urls')),
]

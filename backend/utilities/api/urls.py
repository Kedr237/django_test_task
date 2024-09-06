from django.urls import include, path

urlpatterns = [
    path('v1/utilities/', include('utilities.api.v1.urls')),
]

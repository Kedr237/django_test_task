from django.urls import include, path
from rest_framework.routers import DefaultRouter
from utilities.api.v1 import views

router = DefaultRouter()
router.register(r'buildings', views.BuildingViewSet)
router.register(r'apartments', views.ApartmentViewSet)
router.register(r'tariffs', views.TariffViewSet)
router.register(r'water-meters', views.WaterMeterViewSet)
router.register(r'buildings-info', views.BuildingInfoListView,
                'buildings-info')


urlpatterns = [
    path('', include(router.urls)),
]

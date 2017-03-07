from django.conf.urls import url, include
from rest_framework import routers
from sensor_data.views import PositionMeasurementViewSet

router = routers.DefaultRouter()
router.register(r'position_measurements', PositionMeasurementViewSet)

urlpatterns = [
        url(r'^rest/', include(router.urls)),
        ]

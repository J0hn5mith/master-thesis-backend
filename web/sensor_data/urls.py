from django.conf.urls import url, include
from rest_framework import routers
from sensor_data import views

router = routers.DefaultRouter()
router.register(r'position_measurements', views.PositionMeasurementViewSet)

urlpatterns = [
    url(r'^rest/', include(router.urls)),
    url(
        r'^post/',
        views.post_position_measurement,
        name='post-sensor-data',
    ),
]

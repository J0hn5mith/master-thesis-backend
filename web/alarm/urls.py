from django.conf.urls import url, include
from rest_framework import routers
from alarm.views import AlarmConfigViewSet, AlarmConfigAreaViewSet, \
        AlarmViewSet

router = routers.DefaultRouter()
router.register(r'alarm_config', AlarmConfigViewSet)
router.register(r'alarm_config_area', AlarmConfigAreaViewSet)
router.register(r'alarm', AlarmViewSet)
urlpatterns = [
        url(r'^rest/', include(router.urls)),
        ]

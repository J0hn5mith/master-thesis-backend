from django.conf.urls import url, include
from rest_framework import routers
from alarm import views

router = routers.DefaultRouter()
router.register(r'alarm_config', views.AlarmConfigViewSet)
router.register(r'alarm_config_area', views.AlarmConfigAreaViewSet)
router.register(r'alarm', views.AlarmViewSet)

urlpatterns = [
    url(r'^rest/', include(router.urls)),
    url(
        r'confirm/(?P<random_token>.{10})/',
        views.confirm,
        name='confirm-alarm',
    ),
    url(
        r'cancel/(?P<random_token>.{10})/',
        views.cancel,
        name='cancel-alarm',
    ),
]

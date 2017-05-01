from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet, UserConfigurationViewSet, current_user,\
    LightUserList

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'user_light', LightUserList)
router.register(r'user_config', UserConfigurationViewSet)

urlpatterns = [
    url(r'^rest/', include(router.urls)),
    url(r'^rest/current-user', current_user, name='user-current'),
]

from django.conf.urls import url, include
from rest_framework import routers
from tags.views import TagViewSet

router = routers.DefaultRouter()
router.register(r'tags', TagViewSet)

urlpatterns = [
    url(r'^rest/', include(router.urls)),
]

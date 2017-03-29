from django.conf.urls import url, include
from rest_framework import routers
from tags.views import TagViewSet, tag_prototype_view

router = routers.DefaultRouter()
router.register(r'tags', TagViewSet)

urlpatterns = [
    url(r'^rest/', include(router.urls)),
    url(r'^rest/prototype', tag_prototype_view),
]

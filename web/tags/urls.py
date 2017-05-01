from django.conf.urls import url, include
from rest_framework import routers
from tags.views import TagViewSet, SharedTagViewSet, SharedTagListView

router = routers.DefaultRouter()
router.register(r'tags', TagViewSet)
router.register(r'shared_tags', SharedTagViewSet)

urlpatterns = [
    url(r'^rest/', include(router.urls)),
    url(r'^rest/shared-tag-list', SharedTagListView.as_view()),
]

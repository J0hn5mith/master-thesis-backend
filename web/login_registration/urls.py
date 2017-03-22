from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^activate/(?P<activation_key>\w+)/$',
        views.ActivationView.as_view(),
        name='activate'
    ),
]

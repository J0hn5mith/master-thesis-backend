from django.views.generic import TemplateView
from django.conf.urls import url
from .views import HomeView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
    # url(
        # r'^testtest$',
        # TemplateView.as_view(template_name='login.html'),
        # name='auth_logout'
    # ),
    url(
        r'^technology$',
        TemplateView.as_view(template_name='technology.html'),
        name='technology'
    ),
    url(
        r'^support$',
        TemplateView.as_view(template_name='support.html'),
        name='support'
    ),
    url(
        r'^mail-test$',
        TemplateView.as_view(
            template_name='registration/activation_email.html'
        )
    ),
]

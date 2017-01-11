from django.views.generic import TemplateView
from django.conf.urls import url

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^login$', TemplateView.as_view(template_name='login.html')),
    url(r'^register$', TemplateView.as_view(template_name='register.html')),
    ]

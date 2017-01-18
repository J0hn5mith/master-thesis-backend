from django.views.generic import TemplateView
from django.conf.urls import url

urlpatterns = [
        url(
            r'^$',
            TemplateView.as_view(template_name='dashboard.html'),
            name='dashboard'
            ),
        url(
            r'tags$',
            TemplateView.as_view(template_name='tags.html'),
            name='tags'
            ),
        url(
            r'^notifications$',
            TemplateView.as_view(template_name='notifications.html'),
            name='notifications'
            ),
        url(
            r'^settings$',
            TemplateView.as_view(template_name='settings.html'),
            name='settings'
            ),
        ]

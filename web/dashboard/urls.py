from django.views.generic import TemplateView
from django.conf.urls import url
from dashboard.views import DashboardView, TagsView, NotificationsView, SettingsView

urlpatterns = [
        url(
            r'^$',
            DashboardView.as_view(),
            name='dashboard'
            ),
        url(
            r'tags$',
            TagsView.as_view(),
            name='tags'
            ),
        url(
            r'^notifications$',
            NotificationsView.as_view(),
            name='notifications'
            ),
        url(
            r'^settings$',
            SettingsView.as_view(),
            name='settings'
            ),
        ]

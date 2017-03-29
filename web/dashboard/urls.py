from django.conf.urls import url
from dashboard import views

urlpatterns = [
    url(r'tags$', views.TagsView.as_view(), name='tags'),
    url(
        r'^notifications$',
        views.NotificationsView.as_view(),
        name='notifications'
        ),
    url(r'^settings$', views.SettingsView.as_view(), name='settings'),
    url(r'^', views.DashboardView.as_view(), name='dashboard'),
]

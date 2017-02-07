from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy

class DashboardBaseMixin(LoginRequiredMixin):
    login_url = reverse_lazy('login')


class DashboardView(DashboardBaseMixin, TemplateView):
    template_name = 'dashboard.html'


class TagsView(DashboardBaseMixin, TemplateView):
    template_name = 'tags.html'


class NotificationsView(DashboardBaseMixin, TemplateView):
    template_name='notifications.html'


class SettingsView(DashboardBaseMixin, TemplateView):
    template_name='settings.html'

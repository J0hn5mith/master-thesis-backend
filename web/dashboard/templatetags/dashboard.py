from django import template
from django.core.urlresolvers import reverse

register = template.Library()

class DashboardNavbarItem:
    icon_monochrome = None
    icon = None
    view_name = None
    label = None

    def __init__(self, icon, icon_monochrome, view_name, label, current_url):
        self.icon_monochrome = icon_monochrome
        self.icon = icon
        self.view_name = view_name
        self.label = label
        self.active = reverse(view_name) == current_url


@register.inclusion_tag('partials/dashboard_navbar.html', takes_context=True)
def dashboard_navbar(context):
    current_url = context.request.path
    return {
            'dashboard_items': (
                DashboardNavbarItem(
                    'img/icons/dashboard.svg',
                    'img/icons/dashboard--monochrome.svg',
                    'dashboard',
                    'Dasboard',
                    current_url,
                    ),
                DashboardNavbarItem(
                    'img/icons/tag.svg',
                    'img/icons/tag--monochrome.svg',
                    'tags',
                    'Tags',
                    current_url,
                    ),
                DashboardNavbarItem(
                    'img/icons/message.svg',
                    'img/icons/message--monochrome.svg',
                    'notifications',
                    'Notifications',
                    current_url,
                    ),
                DashboardNavbarItem(
                    'img/icons/settings.svg',
                    'img/icons/settings--monochrome.svg',
                    'settings',
                    'Settings',
                    current_url,
                    ),
                ),
            }

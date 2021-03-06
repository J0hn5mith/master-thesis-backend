"""
master_thesis_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from login_registration.views import LoginView
from django.views.generic.base import RedirectView

urlpatterns = [
        # Hack to redirect after two factor setup
    url(r'^account/two_factor/setup/complete/', RedirectView.as_view(url='/dashboard/', permanent=False)),
    url(r'', include('two_factor.urls', 'two_factor')),
    url(r'', include('registration.backends.default.urls')),
    url(r'^user/', include('user.urls'), name='user'),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls')),
    url(r'^tags/', include('tags.urls'), name='tags'),
    url(r'^sensor-data/', include('sensor_data.urls'), name='sensor-data'),
    url(r'^alarm/', include('alarm.urls'), name='alarm'),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'login/', include('login_registration.urls')),
    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^utils/', include('utils.urls')),

] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

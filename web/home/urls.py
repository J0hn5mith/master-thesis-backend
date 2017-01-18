from django.views.generic import TemplateView
from django.conf.urls import url

urlpatterns = [
        url(r'^$', TemplateView.as_view(template_name='home.html'), name="home"),
        # url(
            # r'^login$',
            # TemplateView.as_view(template_name='login.html'),
            # name='login'

            # ),
        url(
            r'^tmp-register$',
            TemplateView.as_view(template_name='register.html'),
            name="register"
            ),
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
        url(r'^mail-test$',
            TemplateView.as_view(template_name='registration/activation_email.html')),
        ]

from two_factor.views.core import LoginView as BaseLoginView
from registration.backends.default import views as registration_views


class LoginView(BaseLoginView):
    template_name = 'login.html'


class ActivationView(registration_views.ActivationView):
    pass

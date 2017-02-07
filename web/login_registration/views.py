from two_factor.views.core import LoginView as BaseLoginView
from registration.backends.default.views import RegistrationView as BaseRegistrationView


# class RegisterView():

class LoginView(BaseLoginView):
    template_name = 'login.html'
    pass

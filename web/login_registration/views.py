from two_factor.views.core import LoginView as BaseLoginView


class LoginView(BaseLoginView):
    template_name = 'login.html'

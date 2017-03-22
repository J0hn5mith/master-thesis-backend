from django.contrib.auth.decorators import user_passes_test
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator


class HomeView(TemplateView):
    template_name = 'home.html'

    @method_decorator(
        user_passes_test(lambda user: user.is_anonymous, 'dashboard')
    )
    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)

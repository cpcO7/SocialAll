from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = 'apps/login.html'
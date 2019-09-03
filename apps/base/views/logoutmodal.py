# Librerias Django
from django.views.generic import TemplateView


class LogOutModalView(TemplateView):
    template_name = 'base/logoutmodal.html'

# Librerias Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from ...base.models import PyApp

APP_FIELDS = [
    {'string': 'Nombre', 'field': 'name'},
    {'string': 'Author', 'field': 'author'},
    {'string': 'Description', 'field': 'description'},
    {'string': 'Installed', 'field': 'installed'},
]

class AppView(LoginRequiredMixin, ListView):
    model = PyApp
    template_name = 'base/apps.html'
    fields = APP_FIELDS
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
# Librerias Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.edit import UpdateView

# Librerias en carpetas locales
from ..models import BaseConfig


class UpdateBaseConfigView(LoginRequiredMixin,UpdateView):
    login_url = "login"
    model = BaseConfig
    template_name = 'erp/form.html'
    fields = ['online', 'open_menu','main_company_id']


def LoadData(LoginRequiredMixin,request):
    state = BaseConfig.objects.get(pk=1).load_data
    if state:
        print("Ya existe Data")
    else:
        print("Cargamos")
    return render(request, 'base/ok.html')

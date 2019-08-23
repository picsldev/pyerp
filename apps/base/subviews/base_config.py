from django.views.generic.edit import UpdateView
from ..models import BaseConfig
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


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

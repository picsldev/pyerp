from django.views.generic.edit import UpdateView
from ..models import BaseConfig
from django.shortcuts import render


class UpdateBaseConfigView(UpdateView):
    model = BaseConfig
    template_name = 'erp/form.html'
    fields = ['online', 'open_menu','main_company_id']


def LoadData(request):
    state = BaseConfig.objects.get(pk=1).load_data
    if state:
        print("Ya existe Data")
    else:
        print(state)
        print("============================")
        print("Cargando Datos")
        print("============================")
    return render(request, 'base/ok.html')

from django.views.generic.edit import UpdateView
from ..models import BaseConfig
from django.shortcuts import render
from ...dte.submodels.economical_activitie import PyEconomicalActivitie


class UpdateBaseConfigView(UpdateView):
    model = BaseConfig
    template_name = 'erp/form.html'
    fields = ['online', 'open_menu','main_company_id']


def LoadData(request):
    state = BaseConfig.objects.get(pk=1).load_data
    if state:
        print("Ya existe Data")
    else:
        PyEconomicalActivitie(code='011101', name='CULTIVO DE TRIGO').save()
        PyEconomicalActivitie(code='011102', name='CULTIVO DE MAÍZ').save()
        PyEconomicalActivitie(code='011103', name='CULTIVO DE AVENA').save()
        PyEconomicalActivitie(code='011104', name='CULTIVO DE CEBADA').save()
        PyEconomicalActivitie(code='011105', name='CULTIVO DE OTROS CEREALES (EXCEPTO TRIGO, MAÍZ, AVENA Y CEBADA)').save()
    return render(request, 'base/ok.html')

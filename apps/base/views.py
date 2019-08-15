from django.shortcuts import render
from django.views.generic import ListView
from ..base.models import PyPartner, PyCompany


class PartnerListView(ListView):
    model = PyPartner
    template_name = 'erp/list.html'

    def get_context_data(self, **kwargs):
        context = super(PartnerListView, self).get_context_data(**kwargs)
        context['list_name'] = 'Partners'
        context['fields'] = [
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'RUT', 'field': 'rut'},
            {'string': 'Teléfono', 'field': 'phone'},
            {'string': 'Email', 'field': 'email'},
        ]
        return context


class CompanyListView(ListView):
    model = PyCompany
    template_name = 'erp/list.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyListView, self).get_context_data(**kwargs)
        context['list_name'] = 'Compañías'
        context['fields'] = [
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'RUT', 'field': 'rut'},
            {'string': 'Teléfono', 'field': 'phone'},
            {'string': 'Email', 'field': 'email'},
            {'string': 'Giro', 'field': 'giro'},
        ]
        return context

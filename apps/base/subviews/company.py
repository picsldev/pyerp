from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from ...base.models import PyCompany


COMPANY_FIELDS = [
    {'string': 'Nombre', 'field': 'name'},
    {'string': 'RUT', 'field': 'rut'},
    {'string': 'Teléfono', 'field': 'phone'},
    {'string': 'Email', 'field': 'email'},
    {'string': 'Giro', 'field': 'giro'},
]

COMPANY_FIELDS_SHORT = ['name', 'city', 'phone', 'email', 'rut', 'social_facebook', 'social_instagram', 'social_linkedin']


class CompanyListView(ListView):
    model = PyCompany
    template_name = 'erp/list.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyListView, self).get_context_data(**kwargs)
        context['title'] = 'Compañías'
        context['detail_url'] = 'company-detail'
        context['add_url'] = 'company-add'
        context['fields'] = COMPANY_FIELDS
        return context



class CompanyDetailView(DetailView):
    model = PyCompany
    template_name = 'erp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'companies', 'name': 'Compañia'}]
        context['update_url'] = 'company-update'
        context['delete_url'] = 'company-delete'
        context['fields'] = COMPANY_FIELDS
        return context

class CompanyCreateView(CreateView):
    model = PyCompany
    fields = COMPANY_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Compañía'
        context['breadcrumbs'] = [{'url': 'companies', 'name': 'Compañías'}]
        context['back_url'] = reverse('companies')
        return context


class CompanyUpdateView(UpdateView):
    model = PyCompany
    fields = COMPANY_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'companies', 'name': 'Compañías'}]
        context['back_url'] = reverse('company-detail', kwargs={'pk': context['object'].pk})
        return context

@login_required(login_url="/erp/login")
def DeleteCompany(self, pk):
    company = PyCompany.objects.get(id=pk)
    company.delete()
    return redirect(reverse('companies'))

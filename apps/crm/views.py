from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from ..crm.models import PyLead, PyStage
from django.contrib.auth.models import User


def DashboardCrmView(request):
    return render(request, 'crm/dashboard-crm.html')

""" BEGIN LEAD """
LEAD_FIELDS = [
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Cliente', 'field': 'partner_id'},
            {'string': 'Vendedor', 'field': 'user_id'},
            {'string': 'Ingreso', 'field': 'income'},
            {'string': 'Etapa', 'field': 'stage_id'},
        ]

LEAD_FIELDS_SHORT = ['name','partner_id','user_id','income','stage_id']


cont_lead = PyLead.objects.count()

print(cont_lead)



class LeadListView(ListView):
    model = PyLead
    template_name = 'erp/list.html'

    def get_context_data(self, **kwargs):
        context = super(LeadListView, self).get_context_data(**kwargs)
        context['title'] = 'Oportunidades'
        context['detail_url'] = 'lead-detail'
        context['add_url'] = 'lead-add'
        context['fields'] = LEAD_FIELDS
        return context

class LeadDetailView(DetailView):
    model = PyLead
    template_name = 'erp/detail.html'
    def get_context_data(self, **kwargs):
        context = super(LeadDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'lead', 'name': 'Oportunidad'}]
        context['update_url'] = 'lead-update'
        context['delete_url'] = 'lead-delete'
        context['fields'] = LEAD_FIELDS
        return context

class LeadCreateView(CreateView):
    model = PyLead
    fields = LEAD_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(LeadCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Lead'
        context['breadcrumbs'] = [{'url': 'lead', 'name': 'Oportunidad'}]
        context['back_url'] = reverse('lead')
        return context

class LeadUpdateView(UpdateView):
    model = PyLead
    fields = LEAD_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(LeadUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'lead', 'name': 'Oportunidad'}]
        context['back_url'] = reverse('lead-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="/erp/login")
def DeleteLead(self, pk):
    lead = PyLead.objects.get(id=pk)
    lead.delete()
    return redirect(reverse('lead'))
""" END LEAD """



""" BEGIN STAGE """
STAGE_FIELDS = [
            {'string': 'Nombre', 'field': 'name'},
        ]

STAGE_FIELDS_SHORT = ['name']


class StageListView(ListView):
    model = PyStage
    template_name = 'erp/list.html'

    def get_context_data(self, **kwargs):
        context = super(StageListView, self).get_context_data(**kwargs)
        context['title'] = 'Etapas'
        context['detail_url'] = 'stage-detail'
        context['add_url'] = 'stage-add'
        context['fields'] = STAGE_FIELDS
        return context

class StageDetailView(DetailView):
    model = PyStage
    template_name = 'erp/detail.html'
    def get_context_data(self, **kwargs):
        context = super(StageDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'stage', 'name': 'Etapas'}]
        context['update_url'] = 'stage-update'
        context['delete_url'] = 'stage-delete'
        context['fields'] = STAGE_FIELDS
        return context

class StageCreateView(CreateView):
    model = PyStage
    fields = STAGE_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(StageCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Etapa'
        context['breadcrumbs'] = [{'url': 'stage', 'name': 'Etapa'}]
        context['back_url'] = reverse('stage')
        return context

class StageUpdateView(UpdateView):
    model = PyStage
    fields = STAGE_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(StageUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'stage', 'name': 'Etapa'}]
        context['back_url'] = reverse('stage-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="/erp/login")
def DeleteStage(self, pk):
    lead = PyStage.objects.get(id=pk)
    lead.delete()
    return redirect(reverse('stage'))
""" END STAGE """

from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from ..submodels.lead import PyLead
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


""" BEGIN LEAD """
LEAD_FIELDS = [
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Cliente', 'field': 'partner_id'},
            {'string': 'Vendedor', 'field': 'user_id'},
            {'string': 'Ingreso', 'field': 'income'},
            {'string': 'Etapa', 'field': 'stage_id'},
        ]

LEAD_FIELDS_VIEW = [
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Cliente', 'field': 'partner_id'},
            {'string': 'Vendedor', 'field': 'user_id'},
            {'string': 'Ingreso', 'field': 'income'},
            {'string': 'Etapa', 'field': 'stage_id'},
            {'string': 'Canal', 'field': 'channel_id'},
            {'string': 'Campaña', 'field': 'campaign_id'},
        ]

LEAD_FIELDS_SHORT = ['name','partner_id','user_id','income','stage_id','channel_id','campaign_id']


class LeadListView(LoginRequiredMixin, ListView):
    model = PyLead
    template_name = 'erp/list.html'
    login_url = "/erp/login"

    def get_context_data(self, **kwargs):
        context = super(LeadListView, self).get_context_data(**kwargs)
        context['title'] = 'Oportunidades'
        context['detail_url'] = 'lead-detail'
        context['add_url'] = 'lead-add'
        context['fields'] = LEAD_FIELDS_VIEW
        return context

class LeadDetailView(LoginRequiredMixin, DetailView):
    model = PyLead
    template_name = 'erp/detail.html'
    login_url = "/erp/login"
    def get_context_data(self, **kwargs):
        context = super(LeadDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'lead', 'name': 'Oportunidad'}]
        context['update_url'] = 'lead-update'
        context['delete_url'] = 'lead-delete'
        context['fields'] = LEAD_FIELDS_VIEW
        return context

class LeadCreateView(LoginRequiredMixin, CreateView):
    model = PyLead
    fields = LEAD_FIELDS_SHORT
    template_name = 'erp/form.html'
    login_url = "/erp/login"

    def get_context_data(self, **kwargs):
        context = super(LeadCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Lead'
        context['breadcrumbs'] = [{'url': 'lead', 'name': 'Oportunidad'}]
        context['back_url'] = reverse('lead')
        return context

class LeadUpdateView(LoginRequiredMixin, UpdateView):
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
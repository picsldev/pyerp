from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from ..crm.models import PyLead
from django.contrib.auth.models import User

""" BEGIN LEAD """
LEAD_FIELDS = [
            {'string': 'Nombre', 'field': 'name'},
        ]

LEAD_FIELDS_SHORT = ['name']


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

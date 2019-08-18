from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from ..account.models import PyAccountPlan
from django.contrib.auth.models import User


""" BEGIN ACCOUNTPLAN """
ACCOUNTPLAN_FIELDS = [
            {'string': 'Código', 'field': 'code'},
            {'string': 'Nombre', 'field': 'name'},
        ]

ACCOUNTPLAN_FIELDS_SHORT = ['code','name']


class AccountPlanListView(ListView):
    model = PyAccountPlan
    template_name = 'erp/list.html'

    def get_context_data(self, **kwargs):
        context = super(AccountPlanListView, self).get_context_data(**kwargs)
        context['title'] = 'Plan de Cuenta'
        context['detail_url'] = 'accountplan-detail'
        context['add_url'] = 'accountplan-add'
        context['fields'] = ACCOUNTPLAN_FIELDS
        return context

class AccountPlanDetailView(DetailView):
    model = PyAccountPlan
    template_name = 'erp/detail.html'
    def get_context_data(self, **kwargs):
        context = super(AccountPlanDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'accountplan', 'name': 'Cuenta Contable'}]
        context['update_url'] = 'accountplan-update'
        context['delete_url'] = 'accountplan-delete'
        context['fields'] = ACCOUNTPLAN_FIELDS
        return context

class AccountPlanCreateView(CreateView):
    model = PyAccountPlan
    fields = ACCOUNTPLAN_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(AccountPlanCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Cuenta'
        context['breadcrumbs'] = [{'url': 'accountplan', 'name': 'Crear Cuenta'}]
        context['back_url'] = reverse('lead')
        return context

class AccountPlanUpdateView(UpdateView):
    model = PyAccountPlan
    fields = ACCOUNTPLAN_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(AccountPlanUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'accountplan', 'name': 'Cuenta Contable'}]
        context['back_url'] = reverse('accountplan-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="/erp/login")
def DeleteAccountPlan(self, pk):
    accountplan = PyAccountPlan.objects.get(id=pk)
    accountplan.delete()
    return redirect(reverse('accountplan'))
""" END ACCOUNTPLAN """

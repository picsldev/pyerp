from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from ..submodels.accountplan import PyAccountPlan

""" BEGIN ACCOUNTPLAN """
ACCOUNTPLAN_FIELDS = [
            {'string': 'Código', 'field': 'code'},
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Tipo', 'field': 'type'},
            {'string': 'Conciliación', 'field': 'reconcile'},
        ]

ACCOUNTPLAN_FIELDS_SHORT = ['code','name','type', 'reconcile']


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
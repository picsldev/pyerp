# Librerias Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Librerias en carpetas locales
from ..models import PyCurrency

CURRENCY_FIELDS = [
    {'string': 'Nombre', 'field': 'name'},
    {'string': 'Alias', 'field': 'alias'},
    {'string': 'Símbolo', 'field': 'symbol'},
    {'string': 'Posición', 'field': 'position'},
]

CURRENCY_SHORT = ['name', 'alias', 'symbol', 'position']


class CurrencyListView(LoginRequiredMixin, ListView):
    model = PyCurrency
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CurrencyListView, self).get_context_data(**kwargs)
        context['title'] = 'Monedas'
        context['detail_url'] = 'base:currency-detail'
        context['add_url'] = 'base:currency-add'
        context['fields'] = CURRENCY_FIELDS
        return context


class CurrencyDetailView(LoginRequiredMixin, DetailView):
    model = PyCurrency
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CurrencyDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:currencies', 'name': 'Monedas'}]
        context['update_url'] = 'base:currency-update'
        context['delete_url'] = 'base:currency-delete'
        context['fields'] = CURRENCY_FIELDS
        return context


class CurrencyCreateView(LoginRequiredMixin, CreateView):
    model = PyCurrency
    fields = CURRENCY_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CurrencyCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Moneda'
        context['breadcrumbs'] = [{'url': 'base:currencies', 'name': 'Monedas'}]
        context['back_url'] = reverse('base:currencies')
        return context


class CurrencyUpdateView(LoginRequiredMixin, UpdateView):
    model = PyCurrency
    fields = CURRENCY_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CurrencyUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:currencies', 'name': 'Monedas'}]
        context['back_url'] = reverse('base:currency-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteCurrency(self, pk):
    currency = PyCurrency.objects.get(id=pk)
    currency.delete()
    return redirect(reverse('base:currencies'))

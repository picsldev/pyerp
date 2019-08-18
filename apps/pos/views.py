from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from ..pos.models import PyPos
from django.contrib.auth.models import User


""" BEGIN LEAD """
POS_FIELDS = [
            {'string': 'Nombre', 'field': 'name'},
        ]

POS_FIELDS_SHORT = ['name']


class PosListView(ListView):
    model = PyPos
    template_name = 'erp/list.html'

    def get_context_data(self, **kwargs):
        context = super(PosListView, self).get_context_data(**kwargs)
        context['title'] = 'Puntos de Ventas'
        context['detail_url'] = 'pos-detail'
        context['add_url'] = 'pos-add'
        context['fields'] = POS_FIELDS
        return context

class PosDetailView(DetailView):
    model = PyPos
    template_name = 'erp/detail.html'
    def get_context_data(self, **kwargs):
        context = super(PosDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'pos', 'name': 'Punto de Venta'}]
        context['update_url'] = 'pos-update'
        context['delete_url'] = 'pos-delete'
        context['fields'] = POS_FIELDS
        return context

class PosCreateView(CreateView):
    model = PyPos
    fields = POS_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(PosCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Puntos de Venta'
        context['breadcrumbs'] = [{'url': 'pos', 'name': 'Punto de Venta'}]
        context['back_url'] = reverse('pos')
        return context

class PosUpdateView(UpdateView):
    model = PyPos
    fields = POS_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(PosUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'pos', 'name': 'Punto de Venta'}]
        context['back_url'] = reverse('pos-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="/erp/login")
def DeletePos(self, pk):
    pos = PyPos.objects.get(id=pk)
    pos.delete()
    return redirect(reverse('pos'))
""" END LEAD """

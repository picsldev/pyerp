from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from ..submodels.mform import PyMform
from django.contrib.auth.models import User


MFORM_FIELDS = [
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Campaña', 'field': 'campaign_id'},
        ]

MFORM_FIELDS_VIEW = [
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Campaña', 'field': 'campaign_id'},
        ]

MFORM_FIELDS_SHORT = ['name','campaign_id']


class MformListView(ListView):
    model = PyMform
    template_name = 'erp/list.html'

    def get_context_data(self, **kwargs):
        context = super(MformListView, self).get_context_data(**kwargs)
        context['title'] = 'Formularios'
        context['detail_url'] = 'mform-detail'
        context['add_url'] = 'mform-add'
        context['fields'] = MFORM_FIELDS_VIEW
        return context

class MformDetailView(DetailView):
    model = PyMform
    template_name = 'erp/detail.html'
    def get_context_data(self, **kwargs):
        context = super(MformDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'mform', 'name': 'Formulario'}]
        context['update_url'] = 'mform-update'
        context['delete_url'] = 'mform-delete'
        context['fields'] = MFORM_FIELDS_VIEW
        return context

class MformCreateView(CreateView):
    model = PyMform
    fields = MFORM_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(MformCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Formulario'
        context['breadcrumbs'] = [{'url': 'mform', 'name': 'Formulario'}]
        context['back_url'] = reverse('mform')
        return context

class MformUpdateView(UpdateView):
    model = PyMform
    fields = MFORM_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(MformUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'mform', 'name': 'Formulario'}]
        context['back_url'] = reverse('mform-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="/erp/login")
def DeleteMform(self, pk):
    mform = PyMform.objects.get(id=pk)
    mform.delete()
    return redirect(reverse('mform'))
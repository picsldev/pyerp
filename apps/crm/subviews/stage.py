from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from ..submodels.stage import PyStage
from django.contrib.auth.models import User



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
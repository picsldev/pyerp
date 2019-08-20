from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from ..submodels.campaign import PyCampaign
from django.contrib.auth.models import User


CAMPAIGN_FIELDS = [
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Código', 'field': 'code'},
        ]

CAMPAIGN_FIELDS_SHORT = ['name','code']


class CampaignListView(ListView):
    model = PyCampaign
    template_name = 'erp/list.html'

    def get_context_data(self, **kwargs):
        context = super(CampaignListView, self).get_context_data(**kwargs)
        context['title'] = 'Campañas'
        context['detail_url'] = 'campaign-detail'
        context['add_url'] = 'campaign-add'
        context['fields'] = CAMPAIGN_FIELDS
        return context

class CampaignDetailView(DetailView):
    model = PyCampaign
    template_name = 'erp/detail.html'
    def get_context_data(self, **kwargs):
        context = super(CampaignDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'campaign', 'name': 'Campaña'}]
        context['update_url'] = 'campaign-update'
        context['delete_url'] = 'campaign-delete'
        context['fields'] = CAMPAIGN_FIELDS
        return context

class CampaignCreateView(CreateView):
    model = PyCampaign
    fields = CAMPAIGN_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(CampaignCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Campaña'
        context['breadcrumbs'] = [{'url': 'campaign', 'name': 'Campaña'}]
        context['back_url'] = reverse('campaign')
        return context

class CampaignUpdateView(UpdateView):
    model = PyCampaign
    fields = CAMPAIGN_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(CampaignUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'campaign', 'name': 'Campaña'}]
        context['back_url'] = reverse('campaign-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="/erp/login")
def DeleteCampaign(self, pk):
    campaign = PyCampaign.objects.get(id=pk)
    campaign.delete()
    return redirect(reverse('campaign'))
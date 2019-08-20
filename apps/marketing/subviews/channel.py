from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from ..submodels.channel import PyChannel
from django.contrib.auth.models import User


CHANNEL_FIELDS = [
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Código', 'field': 'code'},
        ]

CHANNEL_FIELDS_SHORT = ['name','code']


class ChannelListView(ListView):
    model = PyChannel
    template_name = 'erp/list.html'

    def get_context_data(self, **kwargs):
        context = super(ChannelListView, self).get_context_data(**kwargs)
        context['title'] = 'Canales'
        context['detail_url'] = 'channel-detail'
        context['add_url'] = 'channel-add'
        context['fields'] = CHANNEL_FIELDS
        return context

class ChannelDetailView(DetailView):
    model = PyChannel
    template_name = 'erp/detail.html'
    def get_context_data(self, **kwargs):
        context = super(ChannelDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'channel', 'name': 'Canal'}]
        context['update_url'] = 'channel-update'
        context['delete_url'] = 'channel-delete'
        context['fields'] = CHANNEL_FIELDS
        return context

class ChannelCreateView(CreateView):
    model = PyChannel
    fields = CHANNEL_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(ChannelCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Canal'
        context['breadcrumbs'] = [{'url': 'channel', 'name': 'Canal'}]
        context['back_url'] = reverse('channel')
        return context

class ChannelUpdateView(UpdateView):
    model = PyChannel
    fields = CHANNEL_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(ChannelUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'channel', 'name': 'Canal'}]
        context['back_url'] = reverse('channel-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="/erp/login")
def DeleteChannel(self, pk):
    channel = PyChannel.objects.get(id=pk)
    channel.delete()
    return redirect(reverse('channel'))
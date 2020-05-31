from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from ...base.models import PyLog

LOG_FIELDS = [
    {'string': 'Creado el', 'field': 'created_on'},
    {'string': 'Nombre', 'field': 'name'},
    {'string': 'Notas', 'field': 'note'},
]

LOG_SHORT = ['name','note']


class LogListView(ListView):
    model = PyLog
    template_name = 'erp/list.html'

    def get_context_data(self, **kwargs):
        context = super(LogListView, self).get_context_data(**kwargs)
        context['title'] = 'Logs'
        context['detail_url'] = 'log-detail'
        context['add_url'] = 'log-add'
        context['fields'] = LOG_FIELDS
        return context


class LogDetailView(DetailView):
    model = PyLog
    template_name = 'erp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(LogDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'logs', 'name': 'Logs'}]
        context['update_url'] = 'log-update'
        context['delete_url'] = 'log-delete'
        context['fields'] = LOG_FIELDS
        return context


class LogCreateView(CreateView):
    model = PyLog
    fields = LOG_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(LogCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Log'
        context['breadcrumbs'] = [{'url': 'logs', 'name': 'Logs'}]
        context['back_url'] = reverse('logs')
        return context


class LogUpdateView(UpdateView):
    model = PyLog
    fields = LOG_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(LogUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'logs', 'name': 'Logs'}]
        context['back_url'] = reverse('log-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="/erp/login")
def DeleteLog(self, pk):
    log = PyLog.objects.get(id=pk)
    log.delete()
    return redirect(reverse('logs'))
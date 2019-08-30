from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from ...chat.models import PyTrigger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _

TRIGGER_FIELDS = [
    {'string': _('Question'), 'field': 'question'},
    {'string': _('Answer'), 'field': 'answer'},
    {'string': _('Init'), 'field': 'init'},
]

TRIGGER_SHORT = ['question','answer','init']



class TriggerListView(LoginRequiredMixin, ListView):
    model = PyTrigger
    template_name = 'erp/list.html'
    login_url = "/erp/login"

    def get_context_data(self, **kwargs):
        context = super(TriggerListView, self).get_context_data(**kwargs)
        context['title'] = 'Trigger'
        context['detail_url'] = 'trigger-detail'
        context['add_url'] = 'trigger-add'
        context['fields'] = TRIGGER_FIELDS
        return context


class TriggerDetailView(LoginRequiredMixin, DetailView):
    model = PyTrigger
    template_name = 'erp/detail.html'
    login_url = "/erp/login"

    def get_context_data(self, **kwargs):
        context = super(TriggerDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].question
        context['breadcrumbs'] = [{'url': 'triggers', 'name': 'Triggers'}]
        context['update_url'] = 'trigger-update'
        context['delete_url'] = 'trigger-delete'
        context['fields'] = TRIGGER_FIELDS
        return context


class TriggerCreateView(LoginRequiredMixin, CreateView):
    model = PyTrigger
    fields = TRIGGER_SHORT
    template_name = 'erp/form.html'
    login_url = "/erp/login"

    def get_context_data(self, **kwargs):
        context = super(TriggerCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Trigger'
        context['breadcrumbs'] = [{'url': 'triggers', 'name': 'Triggers'}]
        context['back_url'] = reverse('triggers')
        return context


class TriggersUpdateView(LoginRequiredMixin, UpdateView):
    model = PyTrigger
    fields = TRIGGER_SHORT
    template_name = 'erp/form.html'
    login_url = "/erp/login"

    def get_context_data(self, **kwargs):
        context = super(TriggersUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].question
        context['breadcrumbs'] = [{'url': 'triggers', 'name': 'Triggers'}]
        context['back_url'] = reverse('trigger-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="/erp/login")
def DeleteTrigger(self, pk):
    trigger = PyTrigger.objects.get(id=pk)
    trigger.delete()
    return redirect(reverse('triggers'))
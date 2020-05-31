from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from ..submodels.pos import PyPos
from django.contrib.auth.mixins import LoginRequiredMixin

POS_FIELDS = [
            {'string': 'Nombre', 'field': 'name'},
        ]

POS_FIELDS_SHORT = ['name']


class PosListView(LoginRequiredMixin, ListView):
    model = PyPos
    template_name = 'erp/list.html'
    login_url = "/erp/login"

    def get_context_data(self, **kwargs):
        context = super(PosListView, self).get_context_data(**kwargs)
        context['title'] = 'Puntos de Ventas'
        context['detail_url'] = 'pos-detail'
        context['add_url'] = 'pos-add'
        context['fields'] = POS_FIELDS
        return context

class PosDetailView(LoginRequiredMixin, DetailView):
    model = PyPos
    template_name = 'erp/detail.html'
    login_url = "/erp/login"

    def get_context_data(self, **kwargs):
        context = super(PosDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'pos', 'name': 'Punto de Venta'}]
        context['update_url'] = 'pos-update'
        context['delete_url'] = 'pos-delete'
        context['fields'] = POS_FIELDS
        return context

class PosCreateView(LoginRequiredMixin, CreateView):
    model = PyPos
    fields = POS_FIELDS_SHORT
    template_name = 'erp/form.html'
    login_url = "/erp/login"

    def get_context_data(self, **kwargs):
        context = super(PosCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Puntos de Venta'
        context['breadcrumbs'] = [{'url': 'pos', 'name': 'Punto de Venta'}]
        context['back_url'] = reverse('pos')
        return context

class PosUpdateView(LoginRequiredMixin, UpdateView):
    model = PyPos
    fields = POS_FIELDS_SHORT
    template_name = 'erp/form.html'
    login_url = "/erp/login"

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

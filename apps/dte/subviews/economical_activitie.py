from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView


from ..submodels.economical_activitie import PyEconomicalActivitie

EACT_FIELDS = [
    {'string': 'Código', 'field': 'code'},
    {'string': 'Nombre', 'field': 'name'},
]

EACT_FIELDS_SHORT = ['code','name']


class EconomicalActivitieListView(ListView):
    model = PyEconomicalActivitie
    template_name = 'erp/list.html'

    def get_context_data(self, **kwargs):
        context = super(EconomicalActivitieListView, self).get_context_data(**kwargs)
        context['title'] = 'Actividades Ecónomicas'
        context['detail_url'] = 'economical-activitie-detail'
        context['add_url'] = 'economical-activitie-add'
        context['fields'] = EACT_FIELDS
        return context


class EconomicalActivitieDetailView(DetailView):
    model = PyEconomicalActivitie
    template_name = 'erp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(EconomicalActivitieDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'economical-activitie', 'name': 'Actividad Ecónomica'}]
        context['update_url'] = 'economical-activitie-update'
        context['delete_url'] = 'economical-activitie-delete'
        context['fields'] = EACT_FIELDS
        return context


class EconomicalActivitieCreateView(CreateView):
    model = PyEconomicalActivitie
    fields = EACT_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(EconomicalActivitieCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Actividad Económica'
        context['breadcrumbs'] = [{'url': 'economical-activitie', 'name': 'Actividad Ecónomica'}]
        context['back_url'] = reverse('economical-activitie')
        return context


class EconomicalActivitieUpdateView(UpdateView):
    model = PyEconomicalActivitie
    fields = EACT_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(EconomicalActivitieUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'economical-activitie', 'name': 'Actividad Ecónomica'}]
        context['back_url'] = reverse('economical-activitie-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="/erp/login")
def DeleteEconomicalActivitie(self, pk):
    product_category = PyEconomicalActivitie.objects.get(id=pk)
    product_category.delete()
    return redirect(reverse('economical-activitie'))

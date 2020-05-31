from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from ..submodels.bug import PyBug

""" BEGIN BUG """
BUG_FIELDS = [
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Estado', 'field': 'state'},
            {'string': 'Usuario', 'field': 'user_id'},
            {'string': 'Notas', 'field': 'note'},
        ]

BUG_FIELDS_SHORT = ['name','state','user_id','note']


class BugListView(ListView):
    model = PyBug
    template_name = 'erp/list.html'

    def get_context_data(self, **kwargs):
        context = super(BugListView, self).get_context_data(**kwargs)
        context['title'] = 'Errores'
        context['detail_url'] = 'bug-detail'
        context['add_url'] = 'bug-add'
        context['fields'] = BUG_FIELDS
        return context

class BugDetailView(DetailView):
    model = PyBug
    template_name = 'erp/detail.html'
    def get_context_data(self, **kwargs):
        context = super(BugDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'bug', 'name': 'Error'}]
        context['update_url'] = 'bug-update'
        context['delete_url'] = 'bug-delete'
        context['fields'] = BUG_FIELDS
        return context

class BugCreateView(CreateView):
    model = PyBug
    fields = BUG_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(BugCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Error'
        context['breadcrumbs'] = [{'url': 'bug', 'name': 'Error'}]
        context['back_url'] = reverse('bug')
        return context

class BugUpdateView(UpdateView):
    model = PyBug
    fields = BUG_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(BugUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'bug', 'name': 'Error'}]
        context['back_url'] = reverse('bug-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="/erp/login")
def DeleteBug(self, pk):
    bug = PyBug.objects.get(id=pk)
    bug.delete()
    return redirect(reverse('bug'))
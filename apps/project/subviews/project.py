from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from ..submodels.project import PyProject


PROJECT_FIELDS = [
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Estado', 'field': 'state'},
            {'string': 'Usuario', 'field': 'user_id'},
            {'string': 'Notas', 'field': 'note'},
        ]

PROJECT_FIELDS_SHORT = ['name','state','user_id','note']


class ProjectListView(ListView):
    model = PyProject
    template_name = 'erp/list.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        context['title'] = 'Proyectos'
        context['detail_url'] = 'project-detail'
        context['add_url'] = 'project-add'
        context['fields'] = PROJECT_FIELDS
        return context

class ProjectDetailView(DetailView):
    model = PyProject
    template_name = 'erp/detail.html'
    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'project', 'name': 'Proyecto'}]
        context['update_url'] = 'project-update'
        context['delete_url'] = 'project-delete'
        context['fields'] = PROJECT_FIELDS
        return context

class ProjectCreateView(CreateView):
    model = PyProject
    fields = PROJECT_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Proyecto'
        context['breadcrumbs'] = [{'url': 'project', 'name': 'Proyecto'}]
        context['back_url'] = reverse('project')
        return context

class ProjectUpdateView(UpdateView):
    model = PyProject
    fields = PROJECT_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'project', 'name': 'Proyecto'}]
        context['back_url'] = reverse('project-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="/erp/login")
def DeleteProject(self, pk):
    project = PyProject.objects.get(id=pk)
    project.delete()
    return redirect(reverse('project'))
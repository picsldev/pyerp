from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from ..project.models import PyTask, PyProject, PyBug
from django.contrib.auth.models import User

""" BEGIN TASK """
TASK_FIELDS = [
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Estado', 'field': 'state'},
            {'string': 'Usuario', 'field': 'user_id'},
            {'string': 'Notas', 'field': 'note'},
        ]

TASK_FIELDS_SHORT = ['name','state','user_id','note']


class TaskListView(ListView):
    model = PyTask
    template_name = 'erp/list.html'

    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        context['title'] = 'Tareas'
        context['detail_url'] = 'task-detail'
        context['add_url'] = 'task-add'
        context['fields'] = TASK_FIELDS
        return context

class TaskDetailView(DetailView):
    model = PyTask
    template_name = 'erp/detail.html'
    def get_context_data(self, **kwargs):
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'task', 'name': 'Tarea'}]
        context['update_url'] = 'task-update'
        context['delete_url'] = 'task-delete'
        context['fields'] = TASK_FIELDS
        return context

class TaskCreateView(CreateView):
    model = PyTask
    fields = TASK_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(TaskCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Tarea'
        context['breadcrumbs'] = [{'url': 'task', 'name': 'Tarea'}]
        context['back_url'] = reverse('task')
        return context

class TaskUpdateView(UpdateView):
    model = PyTask
    fields = TASK_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(TaskUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'task', 'name': 'Tarea'}]
        context['back_url'] = reverse('task-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="/erp/login")
def DeleteTask(self, pk):
    task = PyTask.objects.get(id=pk)
    task.delete()
    return redirect(reverse('task'))
""" END TASK """



""" BEGIN PROJECT """
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
""" END PROJECT """





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
""" END BUG """

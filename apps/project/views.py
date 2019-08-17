from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from ..project.models import PyTask
from django.contrib.auth.models import User

""" BEGIN PROJECT """
TASK_FIELDS = [
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Estado', 'field': 'state'},
            {'string': 'Creado', 'field': 'income'},
            {'string': 'Usuario', 'field': 'user_id'},
            {'string': 'Notas', 'field': 'note'},
        ]

TASK_FIELDS_SHORT = ['name','state','income','user_id','note']


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

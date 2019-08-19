from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from ..base.models import (PyDepartment, PyEmployee,
                           PyProduct, PyProductCategory)
from .subviews.partner import CustomerListView, ProviderListView, PartnerDetailView, PartnerCreateView, PartnerUpdateView, DeletePartner
from .subviews.base_config import UpdateBaseConfigView
from .subviews.company import CompanyListView, CompanyDetailView, CompanyCreateView, CompanyUpdateView, DeleteCompany


class UserListView(ListView):
    model = User
    template_name = 'erp/list.html'

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Usuarios'
        context['detail_url'] = 'user-detail'
        context['add_url'] = 'user-add'
        context['fields'] = [
            {'string': 'Login', 'field': 'username'},
            {'string': 'Nombre', 'field': 'first_name'},
            {'string': 'Apellido', 'field': 'last_name'},
            {'string': 'Email', 'field': 'email'},
        ]
        return context


class UserDetailView(DetailView):
    model = User
    template_name = 'erp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].username
        context['breadcrumbs'] = [{'url': 'users', 'name': 'Usuarios'}]
        context['update_url'] = 'user-update'
        context['delete_url'] = 'user-delete'
        context['fields'] = [
            {'string': 'Nombre', 'field': 'first_name'},
            {'string': 'Apellido', 'field': 'last_name'},
            {'string': 'Login', 'field': 'username'},
            {'string': 'Email', 'field': 'email'},
        ]
        context['buttons'] = [
            {
                'act': reverse('password-change', kwargs={'pk': context['object'].pk}),
                'name': 'Cambiar contraseña',
                'class': 'success'
            }
        ]
        return context


class UserCreateView(CreateView):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'password']
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Usuario'
        context['breadcrumbs'] = [{'url': 'users', 'name': 'Usuarios'}]
        context['back_url'] = reverse('users')
        return context


class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name']
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].username
        context['breadcrumbs'] = [{'url': 'users', 'name': 'Usuarios'}]
        context['back_url'] = reverse('user-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="/erp/login")
def DeleteUser(self, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return redirect(reverse('users'))


def ChangePasswordForm(self, pk):
    return render(self, 'erp/change_password.html', {'pk': pk})


def DoChangePassword(self, pk, **kwargs):
    user = User.objects.get(id=pk)
    if user and self.POST['new_password1'] == self.POST['new_password2']:
        user.set_password(self.POST['new_password1'])
    else:
        return render(self, 'erp/change_password.html', {'pk': pk, 'error': 'Las contraseñas no coinciden.'})
    return redirect(reverse('user-detail', kwargs={'pk': pk}))


""" BEGIN EMPLEOYEE """
EMPLEOYEE_FIELDS = [
    {'string': 'Nombre', 'field': 'name'},
    {'string': 'Segundo Nombre', 'field': 'name2'},
    {'string': 'Primer Apelllido', 'field': 'first_name'},
    {'string': 'Segundo Apelllido', 'field': 'last_name'},
    {'string': 'Teléfono', 'field': 'phone'},
    {'string': 'Email', 'field': 'email'},
]

EMPLEOYEE_FIELDS_SHORT = ['name', 'name2', 'email', 'first_name', 'last_name', 'phone', 'email']


class EmployeeListView(ListView):
    model = PyEmployee
    template_name = 'erp/list.html'

    def get_context_data(self, **kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)
        context['title'] = 'Empleados'
        context['detail_url'] = 'employee-detail'
        context['add_url'] = 'employee-add'
        context['fields'] = EMPLEOYEE_FIELDS
        return context


class EmployeeDetailView(DetailView):
    model = PyEmployee
    template_name = 'erp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(EmployeeDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'employee', 'name': 'Empleados'}]
        context['update_url'] = 'employee-update'
        context['delete_url'] = 'employee-delete'
        context['fields'] = EMPLEOYEE_FIELDS
        return context


class EmployeeCreateView(CreateView):
    model = PyEmployee
    fields = EMPLEOYEE_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(EmployeeCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Empleado'
        context['breadcrumbs'] = [{'url': 'employee', 'name': 'Empleado'}]
        context['back_url'] = reverse('employee')
        return context


class EmployeeUpdateView(UpdateView):
    model = PyEmployee
    fields = EMPLEOYEE_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(EmployeeUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'employee', 'name': 'Empleados'}]
        context['back_url'] = reverse('employee-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="/erp/login")
def DeleteEmployee(self, pk):
    employee = PyEmployee.objects.get(id=pk)
    employee.delete()
    return redirect(reverse('employee'))


""" END EMPLEOYEE """


""" BEGIN DEPARTMENT """
DEPARTMENT_FIELDS = [
    {'string': 'Nombre', 'field': 'name'},
]

DEPARTMENT_FIELDS_SHORT = ['name']


class DepartmentListView(ListView):
    model = PyDepartment
    template_name = 'erp/list.html'

    def get_context_data(self, **kwargs):
        context = super(DepartmentListView, self).get_context_data(**kwargs)
        context['title'] = 'Departamentos'
        context['detail_url'] = 'department-detail'
        context['add_url'] = 'department-add'
        context['fields'] = DEPARTMENT_FIELDS
        return context


class DepartmentDetailView(DetailView):
    model = PyDepartment
    template_name = 'erp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DepartmentDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'department', 'name': 'Departamento'}]
        context['update_url'] = 'department-update'
        context['delete_url'] = 'department-delete'
        context['fields'] = DEPARTMENT_FIELDS
        return context


class DepartmentCreateView(CreateView):
    model = PyDepartment
    fields = DEPARTMENT_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(DepartmentCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Departamento'
        context['breadcrumbs'] = [{'url': 'department', 'name': 'Departamento'}]
        context['back_url'] = reverse('department')
        return context


class DepartmentUpdateView(UpdateView):
    model = PyDepartment
    fields = DEPARTMENT_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(DepartmentUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'departmen', 'name': 'Departamento'}]
        context['back_url'] = reverse('departmen-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="/erp/login")
def DeleteDepartment(self, pk):
    department = PyDepartment.objects.get(id=pk)
    department.delete()
    return redirect(reverse('department'))


""" END DEPARTMENT """

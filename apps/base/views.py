from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from ..base.models import PyProduct, PyProductCategory
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

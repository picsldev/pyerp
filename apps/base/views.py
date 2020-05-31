# Librerias Django
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from os import listdir
import json
from .submodels.app import PyApp
from ..base.models import PyPartner, PyProduct, PyApp

# Librerias en carpetas locales
from ..base.models import PyProduct, PyProductCategory
from .subviews.base_config import UpdateBaseConfigView
from .subviews.company import (
    CompanyCreateView, CompanyDetailView, CompanyListView, CompanyUpdateView,
    DeleteCompany)
from .subviews.partner import (
    CustomerListView, DeletePartner, PartnerAutoComplete, PartnerCreateView,
    PartnerDetailView, PartnerUpdateView, ProviderListView)

def Apps(request):
    return render(request, 'base/apps.html')

class UserListView(ListView):
    model = User
    template_name = 'base/list.html'


    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Usuarios'
        context['detail_url'] = 'user-detail'
        context['add_url'] = 'user-add'
        context['fields'] = [
            {'string': _('User Name'), 'field': 'username'},
            {'string': _('Name'), 'field': 'first_name'},
            {'string': _('Last name'), 'field': 'last_name'},
            {'string': _('Email'), 'field': 'email'},
        ]
        return context


class UserDetailView(DetailView):
    model = User
    template_name = 'base/detail.html'

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].username
        context['breadcrumbs'] = [{'url': 'users', 'name': 'Usuarios'}]
        context['update_url'] = 'user-update'
        context['delete_url'] = 'user-delete'
        context['fields'] = [
            {'string': _('User Name'), 'field': 'username'},
            {'string': _('Name'), 'field': 'first_name'},
            {'string': _('Last name'), 'field': 'last_name'},
            {'string': _('Email'), 'field': 'email'},
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
    template_name = 'base/form.html'

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Usuario'
        context['breadcrumbs'] = [{'url': 'users', 'name': 'Usuarios'}]
        context['back_url'] = reverse('users')
        return context


class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name']
    template_name = 'base/form.html'

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].username
        context['breadcrumbs'] = [{'url': 'users', 'name': 'Usuarios'}]
        context['back_url'] = reverse('user-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="/base/login")
def DeleteUser(self, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return redirect(reverse('users'))


def ChangePasswordForm(self, pk):
    return render(self, 'base/change_password.html', {'pk': pk})


def DoChangePassword(self, pk, **kwargs):
    user = User.objects.get(id=pk)
    if user and self.POST['new_password1'] == self.POST['new_password2']:
        user.set_password(self.POST['new_password1'])
    else:
        return render(self, 'base/change_password.html', {'pk': pk, 'error': 'Las contraseñas no coinciden.'})
    return redirect(reverse('user-detail', kwargs={'pk': pk}))


@login_required(login_url="/base/login")
def UpdateApps(self):
    FILE_NAME ='py_info.json'
    folder_apps = 'apps'
    list_app = listdir(folder_apps)
    PyApp.objects.all().delete()
    for folder in list_app:
        try:
            for file in listdir(folder_apps + "/" + folder + "/py"):
                if file == FILE_NAME:
                    with open(folder_apps + "/" + folder + "/py/" + FILE_NAME) as json_file:
                        data = json.load(json_file)
                        p = PyApp(name=data['name'], description=data['description'], author=data['author'],
                                  fa=data['fa'], version=data['version'],
                                  website=data['website'], color=data['color'])
                        p.save()
        except Exception:
            continue


    return redirect(reverse('apps'))


@login_required(login_url="/base/login")
def InstallApps(self, pk):
    app = PyApp.objects.get(id=pk)
    app.installed = True
    app.save()
    return redirect(reverse('apps'))


@login_required(login_url="/base/login")
def UninstallApps(self, pk):
    app = PyApp.objects.get(id=pk)
    app.installed = False
    app.save()
    return redirect(reverse('apps'))

@login_required(login_url="/base/login")
def erp_home(request):
    """Vista para renderizar el dasboard del erp
    """

    count_app = PyApp.objects.all().count()


    apps = PyApp.objects.all().filter(installed=True).order_by('sequence')
    # apps = PyApp.objects.all().order_by('sequence')
    app_list = []
    if apps:
        for app in apps:
            st = app.name + "/menu.html"
            app_list.append(st.lower())

    partners = PyPartner.objects.all()
    return render(request, "home.html", {
        'customers': partners.filter(customer=True),
        'providers': partners.filter(provider=True),
        'users': User.objects.all(),
        'products': PyProduct.objects.all(),
        'app_list' : app_list,
        'count_app' : count_app
    })

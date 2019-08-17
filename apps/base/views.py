from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from ..base.models import PyPartner, PyCompany, PyProduct, PyEmployee, PyDepartment, PyLead
from django.contrib.auth.models import User


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


""" BEGIN PARTNER """

PARTNER_FIELDS  = [
            {'string': 'RUT', 'field': 'rut'},
            {'string': 'Nombre / Razón Social', 'field': 'name'},
            {'string': 'Dirección', 'field': 'street'},
            {'string': 'Teléfono', 'field': 'phone'},
            {'string': 'Email', 'field': 'email'},
            {'string': 'Para Facturar', 'field': 'for_invoice'},
            {'string': 'Creado por', 'field': 'created_by'},
            {'string': 'Creado', 'field': 'created_on'},
            {'string': 'Notas', 'field': 'note'},
        ]

PARTNER_FIELDS_SHORT = [ 'rut', 'name', 'street', 'email', 'phone', 'note', 'customer', 'provider', 'for_invoice']


class CustomerListView(ListView):
    model = PyPartner
    template_name = 'erp/list.html'
    queryset = PyPartner.objects.filter(customer=True).all()

    def get_context_data(self, **kwargs):
        context = super(CustomerListView, self).get_context_data(**kwargs)
        context['title'] = 'Partners'
        context['detail_url'] = 'partner-detail'
        context['add_url'] = 'partner-add'
        context['fields'] = PARTNER_FIELDS
        return context

class ProviderListView(ListView):
    model = PyPartner
    template_name = 'erp/list.html'
    queryset = PyPartner.objects.filter(provider=True).all()

    def get_context_data(self, **kwargs):
        context = super(ProviderListView, self).get_context_data(**kwargs)
        context['title'] = 'Partners'
        context['detail_url'] = 'partner-detail'
        context['add_url'] = 'partner-add'
        context['fields'] = PARTNER_FIELDS
        return context



class PartnerDetailView(DetailView):
    model = PyPartner
    template_name = 'erp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(PartnerDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'partners', 'name': 'Partners'}]
        context['update_url'] = 'partner-update'
        context['delete_url'] = 'partner-delete'
        context['fields'] = PARTNER_FIELDS
        return context


class PartnerCreateView(CreateView):
    model = PyPartner
    fields = ['name', 'email', 'phone', 'rut', 'customer', 'provider']
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(PartnerCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear partner'
        context['breadcrumbs'] = [{'url': 'partners', 'name': 'Partners'}]
        context['back_url'] = reverse('partners')
        return context


class PartnerUpdateView(UpdateView):
    model = PyPartner
    fields = PARTNER_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(PartnerUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'partners', 'name': 'Partners'}]
        context['back_url'] = reverse('partner-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="/erp/login")
def DeletePartner(self, pk):
    partner = PyPartner.objects.get(id=pk)
    partner.delete()
    return redirect(reverse('partners'))





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




class CompanyListView(ListView):
    model = PyCompany
    template_name = 'erp/list.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyListView, self).get_context_data(**kwargs)
        context['title'] = 'Compañías'
        context['fields'] = [
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'RUT', 'field': 'rut'},
            {'string': 'Teléfono', 'field': 'phone'},
            {'string': 'Email', 'field': 'email'},
            {'string': 'Giro', 'field': 'giro'},
        ]
        return context

PRODUCT_FIELDS = [
            {'string': 'Código', 'field': 'code'},
            {'string': 'Código Barra', 'field': 'bar_code'},
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Precio', 'field': 'price'},
            {'string': 'Costo', 'field': 'cost'},
            {'string': 'tipo', 'field': 'type'},
        ]

LEAD_FIELDS_SHORT = ['name', 'code', 'price', 'cost', 'type', 'web_active']


class ProductListView(ListView):
    model = PyProduct
    template_name = 'erp/list.html'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'Productos'
        context['detail_url'] = 'product-detail'
        context['add_url'] = 'product-add'
        context['fields'] = PRODUCT_FIELDS
        return context


class ProductDetailView(DetailView):
    model = PyProduct
    template_name = 'erp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'products', 'name': 'Productos'}]
        context['detail_name'] = 'Producto: %s' % context['object'].name
        context['update_url'] = 'product-update'
        context['delete_url'] = 'product-delete'
        context['fields'] = PRODUCT_FIELDS
        return context



class ProductCreateView(CreateView):
    model = PyProduct
    fields = LEAD_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear producto'
        context['breadcrumbs'] = [{'url': 'products', 'name': 'Productos'}]
        context['back_url'] = reverse('products')
        return context


class ProductUpdateView(UpdateView):
    model = PyProduct
    fields = LEAD_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'products', 'name': 'Productos'}]
        context['back_url'] = reverse('product-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="/erp/login")
def DeleteProduct(self, pk):
    product = PyProduct.objects.get(id=pk)
    product.delete()
    return redirect(reverse('products'))

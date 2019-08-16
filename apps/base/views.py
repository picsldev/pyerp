from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from ..base.models import PyPartner, PyCompany, PyProduct


class PartnerListView(ListView):
    model = PyPartner
    template_name = 'erp/list.html'

    def get_context_data(self, **kwargs):
        context = super(PartnerListView, self).get_context_data(**kwargs)
        context['list_name'] = 'Partners'
        context['detail_url'] = 'partner-detail'
        context['add_url'] = 'partner-add'
        context['fields'] = [
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'RUT', 'field': 'rut'},
            {'string': 'Teléfono', 'field': 'phone'},
            {'string': 'Email', 'field': 'email'},
        ]
        return context


class PartnerDetailView(DetailView):
    model = PyPartner
    template_name = 'erp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(PartnerDetailView, self).get_context_data(**kwargs)
        context['detail_name'] = 'Partner: %s' % context['object'].name
        context['update_url'] = 'partner-update'
        context['delete_url'] = 'partner-delete'
        context['fields'] = [
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'RUT', 'field': 'rut'},
            {'string': 'Teléfono', 'field': 'phone'},
            {'string': 'Email', 'field': 'email'},
        ]
        return context


class PartnerCreateView(CreateView):
    model = PyPartner
    fields = ['name', 'email', 'phone', 'rut']
    template_name = 'erp/form.html'


class PartnerUpdateView(UpdateView):
    model = PyPartner
    fields = ['name', 'email', 'phone', 'rut']
    template_name = 'erp/form.html'


@login_required(login_url="/erp/login")
def DeletePartner(self, pk):
    partner = PyPartner.objects.get(id=pk)
    partner.delete()
    return redirect(reverse('partners'))


class CompanyListView(ListView):
    model = PyCompany
    template_name = 'erp/list.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyListView, self).get_context_data(**kwargs)
        context['list_name'] = 'Compañías'
        context['fields'] = [
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'RUT', 'field': 'rut'},
            {'string': 'Teléfono', 'field': 'phone'},
            {'string': 'Email', 'field': 'email'},
            {'string': 'Giro', 'field': 'giro'},
        ]
        return context


class ProductListView(ListView):
    model = PyProduct
    template_name = 'erp/list.html'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['list_name'] = 'Productos'
        context['detail_url'] = 'product-detail'
        context['add_url'] = 'product-add'
        context['fields'] = [
            {'string': 'Código', 'field': 'code'},
            {'string': 'Código Barra', 'field': 'bar_code'},
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Precio', 'field': 'price'},
            {'string': 'Costo', 'field': 'cost'},
        ]
        return context


class ProductDetailView(DetailView):
    model = PyProduct
    template_name = 'erp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['detail_name'] = 'Producto: %s' % context['object'].name
        context['update_url'] = 'product-update'
        context['delete_url'] = 'product-delete'
        context['fields'] = [
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Código', 'field': 'code'},
            {'string': 'Precio', 'field': 'price'},
            {'string': 'Costo', 'field': 'cost'},
        ]
        return context

PRODUCT_FIELDS = ['name', 'code', 'price', 'cost']

class ProductCreateView(CreateView):
    model = PyProduct
    fields = PRODUCT_FIELDS
    template_name = 'erp/form.html'


class ProductUpdateView(UpdateView):
    model = PyProduct
    fields = PRODUCT_FIELDS
    template_name = 'erp/form.html'


@login_required(login_url="/erp/login")
def DeleteProduct(self, pk):
    product = PyProduct.objects.get(id=pk)
    product.delete()
    return redirect(reverse('products'))

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from ...base.models import PyProduct


PRODUCT_FIELDS = [
    {'string': 'Código', 'field': 'code'},
    {'string': 'Código Barra', 'field': 'bar_code'},
    {'string': 'Nombre', 'field': 'name'},
    {'string': 'Categoría', 'field': 'category_id'},
    {'string': 'Precio', 'field': 'price'},
    {'string': 'Costo', 'field': 'cost'},
    {'string': 'tipo', 'field': 'type'},
    {'string': 'Creado', 'field': 'created_on'},
    {'string': 'Descripción', 'field': 'description'},
    {'string': 'Creado', 'field': 'created_on'},
]

LEAD_FIELDS_SHORT = ['name', 'category_id', 'code', 'price', 'cost', 'type', 'description', 'web_active']


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
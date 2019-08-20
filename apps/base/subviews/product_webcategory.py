from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from ...base.models import PyProductWebCategory

""" BEGIN CATEGORY PRODUCT"""
CATEGORY_FIELDS = [
    {'string': 'Nombre', 'field': 'name'},
]

CATEGORY_FIELDS_SHORT = ['name']


class ProductWebCategoryListView(ListView):
    model = PyProductWebCategory
    template_name = 'erp/list.html'

    def get_context_data(self, **kwargs):
        context = super(ProductWebCategoryListView, self).get_context_data(**kwargs)
        context['title'] = 'Categorías Web de Productos'
        context['detail_url'] = 'product-webcategory-detail'
        context['add_url'] = 'product-webcategory-add'
        context['fields'] = CATEGORY_FIELDS
        return context


class ProductWebCategoryDetailView(DetailView):
    model = PyProductWebCategory
    template_name = 'erp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductWebCategoryDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'product-webcategory', 'name': 'Categorias Web de Productos'}]
        context['update_url'] = 'product-webcategory-update'
        context['delete_url'] = 'product-webcategory-delete'
        context['fields'] = CATEGORY_FIELDS
        return context


class ProductWebCategoryCreateView(CreateView):
    model = PyProductWebCategory
    fields = CATEGORY_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(ProductWebCategoryCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Categoria Web de Productos'
        context['breadcrumbs'] = [{'url': 'product-webcategory', 'name': 'Categoria Web de Producto'}]
        context['back_url'] = reverse('product-category')
        return context


class ProductWebCategoryUpdateView(UpdateView):
    model = PyProductWebCategory
    fields = CATEGORY_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(ProductWebCategoryUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'product-webcategory', 'name': 'Categoria Web de Producto'}]
        context['back_url'] = reverse('product-webcategory-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="/erp/login")
def DeleteProductWebCategory(self, pk):
    product_category = PyProductWebCategory.objects.get(id=pk)
    product_category.delete()
    return redirect(reverse('product-webcategory'))


""" END CATEGORY PRODUCT """


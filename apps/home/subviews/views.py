from __future__ import unicode_literals
from apps.website.submodels.post import PyPost
from apps.base.submodels.product import PyProduct
from django.views.generic import DetailView, ListView
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def post(request):
    return render(request, 'post.html')

def license(request):
    return render(request, 'license.html')

def UnderConstruction(request):
    return render(request, 'under_construction.html')

"""
BLOG
"""

POST_FIELDS = [
            {'string': 'Título', 'field': 'title'},
            {'string': 'Creado en', 'field': 'created_on'},
            {'string': 'Contenido', 'field': 'content'},
        ]

POST_FIELDS_SHORT = ['title','content','created_on']

class BlogView(ListView):
    model = PyPost
    template_name = 'blog.html'
    fields = POST_FIELDS
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PostDetailView(DetailView):
    model = PyPost
    template_name = 'post.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



# Tienda de Productos

PRODUCT_FIELDS = [
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Descripción', 'field': 'description'},
            {'string': 'Precio', 'field': 'price'},
            {'string': 'Activo', 'field': 'web_active'},
        ]

class WebProductView(ListView):
    model = PyProduct
    template_name = 'shop.html'
    fields = PRODUCT_FIELDS
    paginate_by = 8
    queryset = PyProduct.objects.filter(web_active='True')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class WebProductDetailView(DetailView):
    model = PyProduct
    template_name = 'product.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
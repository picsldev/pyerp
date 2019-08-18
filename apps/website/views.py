from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from ..website.models import PyArticle
from django.contrib.auth.models import User


""" ARTICLE LEAD """
ARTICLE_FIELDS = [
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Descripción', 'field': 'description'},
        ]

ARTICLE_FIELDS_SHORT = ['name','description']

class ArticleListView(ListView):
    model = PyArticle
    template_name = 'erp/list.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['title'] = 'Artículos'
        context['detail_url'] = 'article-detail'
        context['add_url'] = 'article-add'
        context['fields'] = ARTICLE_FIELDS
        return context

class ArticleDetailView(DetailView):
    model = PyArticle
    template_name = 'erp/detail.html'
    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'article', 'name': 'Artículos'}]
        context['update_url'] = 'article-update'
        context['delete_url'] = 'article-delete'
        context['fields'] = ARTICLE_FIELDS
        return context

class ArticleCreateView(CreateView):
    model = PyArticle
    fields = ARTICLE_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Artículo'
        context['breadcrumbs'] = [{'url': 'article', 'name': 'Artículo'}]
        context['back_url'] = reverse('article')
        return context

class ArticleUpdateView(UpdateView):
    model = PyArticle
    fields = ARTICLE_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'article', 'name': 'Artículo'}]
        context['back_url'] = reverse('article-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="/erp/login")
def DeleteArticle(self, pk):
    article = PyArticle.objects.get(id=pk)
    article.delete()
    return redirect(reverse('article'))
""" END ARTICLE """

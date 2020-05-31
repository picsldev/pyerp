from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from ..submodels.post import PyPost

POST_FIELDS = [
            {'string': 'Título', 'field': 'title'},
            {'string': 'Creado en', 'field': 'created_on'},
        ]

POST_FIELDS_SHORT = ['title','content']

class PostListView(ListView):
    model = PyPost
    template_name = 'erp/list.html'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['title'] = 'Entradas'
        context['detail_url'] = 'post-detail'
        context['add_url'] = 'post-add'
        context['fields'] = POST_FIELDS
        return context

class PostDetailView(DetailView):
    model = PyPost
    template_name = 'erp/detail.html'
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].title
        context['breadcrumbs'] = [{'url': 'post', 'name': 'Entradas'}]
        context['update_url'] = 'post-update'
        context['delete_url'] = 'post-delete'
        context['fields'] = POST_FIELDS
        return context

class PostCreateView(CreateView):
    model = PyPost
    fields = POST_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Post'
        context['breadcrumbs'] = [{'url': 'post', 'name': 'Entrada'}]
        context['back_url'] = reverse('post')
        return context

class PostUpdateView(UpdateView):
    model = PyPost
    fields = POST_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(PostUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].title
        context['breadcrumbs'] = [{'url': 'post', 'name': 'Entrada'}]
        context['back_url'] = reverse('post-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="/erp/login")
def DeletePost(self, pk):
    post = PyPost.objects.get(id=pk)
    post.delete()
    return redirect(reverse('post'))
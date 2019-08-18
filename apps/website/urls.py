from django.urls import path
from django.contrib.auth import views as auth_views
from ..website.views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, DeleteArticle


urlpatterns = [
    path('article', ArticleListView.as_view(), name='article'),
    path('article/add/', ArticleCreateView.as_view(), name='article-add'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('article/<int:pk>/update', ArticleUpdateView.as_view(), name='article-update'),
    path('article/<int:pk>/delete/', DeleteArticle, name='article-delete'),
]
from django.urls import path
from django.contrib.auth import views as auth_views
from .subviews.post import PostListView, PostDetailView, PostCreateView, PostUpdateView, DeletePost
from .subviews.website_config import UpdateWebsiteConfigView


urlpatterns = [
    path('post', PostListView.as_view(), name='post'),
    path('post/add/', PostCreateView.as_view(), name='post-add'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', DeletePost, name='post-delete'),

    path('config/<int:pk>', UpdateWebsiteConfigView.as_view(), name='website-config'),
]
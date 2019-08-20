from django.conf.urls import url
from django.urls import path
from .subviews.views import index, BlogView, PostDetailView,  shop, UnderConstruction

urlpatterns = [
    url(r'^$', index, name='home-index'),
    path('blog/', BlogView.as_view(), name='home-blog'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post'),
    url(r'^shop/', shop, name='home-shop'),
    url(r'^license/', license, name='home-license'),
    url(r'^under-construction/', UnderConstruction, name='under-construction'),
]
from django.conf.urls import url
from django.urls import path
from ..home.views import index, blog, shop, post

urlpatterns = [
    url(r'^$', index, name='home-index'),
    url(r'^blog/', blog, name='home-blog'),
    path('post/<int:post_id>/', post, name="post"),
    url(r'^shop/', shop, name='home-shop'),
    url(r'^license/', license, name='home-license'),
]
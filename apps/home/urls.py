from django.conf.urls import url

from ..home.views import index, blog, shop

urlpatterns = [
    url(r'^$', index, name='home-index'),
    url(r'^blog/', blog, name='home-blog'),
    url(r'^shop/', shop, name='home-shop'),
]
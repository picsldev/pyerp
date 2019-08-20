from django.conf.urls import url

from ..home.views import index, blog, shop, post, license

urlpatterns = [
    url(r'^$', index, name='home-index'),
    url(r'^blog/', blog, name='home-blog'),
    url(r'^shop/', shop, name='home-shop'),
    url(r'^post/', post, name='home-post'),
    url(r'^license/', license, name='home-license'),
]
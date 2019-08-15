from django.conf.urls import url
from ..erp.views import login_user, erp_home, logout_user, auth


urlpatterns = [
    url(r'^$', erp_home),
    url(r'^logout$', logout_user),
    url(r'^auth$', auth),
    url(r'^login$', login_user),   
]
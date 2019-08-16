from django.conf.urls import url
from ..erp.views import login_user, erp_home, logout_user, auth


urlpatterns = [
    url(r'^$', erp_home, name='home'),
    url(r'^logout$', logout_user, name='logout'),
    url(r'^auth$', auth, name='auth'),
    url(r'^login$', login_user, name='login'),
]

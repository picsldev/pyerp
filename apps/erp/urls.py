from django.conf.urls import url
from ..erp.views import login_user


urlpatterns = [
    # url(r'^home$', erp_home),
    url(r'^login$', login_user),    
]
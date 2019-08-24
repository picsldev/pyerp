from django.conf.urls import url
from ..erp.views import erp_home
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    url(r'^$', erp_home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login.html'), name = 'logout')
]

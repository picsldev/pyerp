"""Rutas del modulo erp
"""
# Librerias Django
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path

# Librerias de terceros
from apps.erp.views import LogOutModalView

# Librerias en carpetas locales
from ..erp.views import erp_home

app_name = 'erp'

urlpatterns = [
    path('', erp_home, name='home'),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='login.html'),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(template_name='erp/login.html'),
        name='logout'
    ),
    path('logoutmodal/', LogOutModalView.as_view(), name='logout-modal')
]

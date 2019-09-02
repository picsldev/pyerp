"""Vistas del módulo erp
"""
# Librerias Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

# Librerias en carpetas locales
from ..base.models import PyPartner, PyProduct, PyApp
from .subviews.logoutmodal import LogOutModalView


@login_required(login_url="/erp/login")
def erp_home(request):
    """Vista para renderizar el dasboard del erp
    """
    apps = PyApp.objects.all().filter(installed=True)
    app_list = []
    if apps:
        for app in apps:
            st = app.name + "/menu.html"
            app_list.append(st.lower())

    partners = PyPartner.objects.all()
    return render(request, "home.html", {
        'customers': partners.filter(customer=True),
        'providers': partners.filter(provider=True),
        'users': User.objects.all(),
        'products': PyProduct.objects.all(),
        'app_list' : app_list
    })

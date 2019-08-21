"""pyerp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.apps import apps
from cruds_adminlte.urls import crud_for_app




urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('apps.home.urls')),
    url(r'^erp/', include('apps.erp.urls')),
    url(r'^base/', include('apps.base.urls')),
    url(r'^crm/', include('apps.crm.urls')),
    url(r'^project/', include('apps.project.urls')),
    url(r'^website/', include('apps.website.urls')),
    url(r'^account/', include('apps.account.urls')),
    url(r'^pos/', include('apps.pos.urls')),
    url(r'^marketing/', include('apps.marketing.urls')),
    url(r'^payroll/', include('apps.payroll.urls')),
]

urlpatterns += crud_for_app('account')
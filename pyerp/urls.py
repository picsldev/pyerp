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
# Librerias Django
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^i18n/', include('django.conf.urls.i18n')),
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
    url(r'^sale/', include('apps.sale.urls')),
    url(r'^pychat/', include('apps.chat.urls')),
]

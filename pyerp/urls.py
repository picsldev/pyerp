"""Rutas de PyErp
"""
# Librerias Django
from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls')),
    path('base/', include('apps.base.urls')),
    path('crm/', include('apps.crm.urls')),
    # path('project/', include('apps.project.urls')),
    path('website/', include('apps.website.urls')),
    # path('account/', include('apps.account.urls')),
    # path('pos/', include('apps.pos.urls')),
    path('marketing/', include('apps.marketing.urls')),
    # path('payroll/', include('apps.payroll.urls')),
    path('sale/', include('apps.sale.urls')),
    # path('chat/', include('apps.chat.urls')),
    # path('purchase/', include('apps.purchase.urls')),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT, }),
    path('static/<path:path>', serve, {'document_root': settings.STATIC_ROOT, }),
]


with open('/home/django/pyerp/installed_apps.py', 'r') as ins_apps_file:
    for line in ins_apps_file.readlines():
        app, _ = line.split('.')
        urlpatterns += [path('%s/' % app, include('%s.urls' % line.strip()))]

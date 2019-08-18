from django.contrib import admin
from apps.base.models import PyPartner, PyProduct, PyCountry, PyProductCategory, PyCompany

admin.site.register(PyPartner)
admin.site.register(PyProduct)
admin.site.register(PyCountry)
admin.site.register(PyProductCategory)
admin.site.register(PyCompany)
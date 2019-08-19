from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from .submodels.partner import PyPartner
from .submodels.base_config import BaseConfig
from .submodels.company import PyCompany
from .submodels.locations import PyComuna, PyCountry, PyRegion

from .submodels.product import PyProduct
from .submodels.product_category import PyProductCategory

from datetime import datetime, timedelta
from django.utils.timesince import timesince


# Tabla de Leads
class PyLead(models.Model):
    name = models.CharField('Nombre', max_length=80)

    def get_absolute_url(self):
        return reverse('lead-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.name)

# Tabla de Artículos
class PyArticle(models.Model):
    name = models.CharField('Artículo', max_length=80)

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.name)



# Tabla de Empleados
class PyEmployee(models.Model):
    name = models.CharField('Nombre', max_length=80)
    name2 = models.CharField('Segundo Nombre', max_length=80, blank=True)
    first_name = models.CharField('Apellido Paterno', max_length=80, blank=True)
    last_name = models.CharField('Apellido Materno', max_length=80, blank=True)
    phone = models.CharField('Teléfono', max_length=20, blank=True)
    email = models.CharField('Correo', max_length=40, blank=True)

    def get_absolute_url(self):
        return reverse('employee-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.name)

# Tabla de Departamentos
class PyDepartment(models.Model):
    name = models.CharField('Nombre', max_length=80)

    def get_absolute_url(self):
        return reverse('department-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.name)


from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from .submodels.partner import PyPartner
from .submodels.base_config import BaseConfig
from .submodels.company import PyCompany
from .submodels.locations import PyComuna, PyCountry, PyRegion

from datetime import datetime, timedelta
from django.utils.timesince import timesince


PRODUCT_CHOICE = (
        ("product", "Almacenable"),
        ('consu', 'Consumible'),
        ('service', 'Servicio')
    )


class PyProductCategory(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return format(self.name)

    def get_absolute_url(self):
        return reverse('product-category-detail', kwargs={'pk': self.pk})


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



# Tabla de Product
class PyProduct(models.Model):
    name = models.CharField('Nombre', max_length=80)
    code = models.CharField('Código', max_length=80, blank=True)
    bar_code = models.CharField('Cod. Barras', max_length=80, blank=True)
    price = models.DecimalField('Precio', max_digits=10, decimal_places=2, default=1)
    cost = models.DecimalField('Costo', max_digits=10, decimal_places=2, default=0)
    category_id = models.ForeignKey(PyProductCategory, null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    web_active = models.BooleanField('Web', default=False)

    type = models.CharField(
        choices=PRODUCT_CHOICE, max_length=64, default='consu')

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})

    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)

    def __str__(self):
        return format(self.name)

    class Meta:
        ordering = ['created_on']



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


# Librerias Django
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias de terceros
from apps.base.models import PyFather


# Tabla de Departamentos
class PyDepartment(PyFather):
    name = models.CharField('Nombre', max_length=80)

    def get_absolute_url(self):
        return reverse('base:department-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.name)

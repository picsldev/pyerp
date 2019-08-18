from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Tabla de Leads
class PyAccountPlan(models.Model):
    code = models.CharField('Código', max_length=80)
    name = models.CharField('Nombre', max_length=80)

    def get_absolute_url(self):
        return reverse('accountplan-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return + "[" + format(self.code) + "] " + format(self.name)
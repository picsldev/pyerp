from django.db import models
from django.urls import reverse

# Tabla de Product
class PyEconomicalActivitie(models.Model):
    name = models.CharField('Nombre', max_length=50)
    code = models.CharField('Código', max_length=255)

    def get_absolute_url(self):
        return reverse('economical-activitie-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.name)
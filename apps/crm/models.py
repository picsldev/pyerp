from django.db import models
from django.urls import reverse

# Tabla de Leads
class PyLead(models.Model):
    name = models.CharField('Nombre', max_length=80)

    def get_absolute_url(self):
        return reverse('lead-detail', kwargs={'pk': self.pk})
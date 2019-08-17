from django.db import models
from django.urls import reverse
from ..base.models import PyPartner


# Tabla de Leads
class PyLead(models.Model):
    name = models.CharField('Nombre', max_length=80)
    partner_id = models.ForeignKey(PyPartner, null=True, blank=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('lead-detail', kwargs={'pk': self.pk})
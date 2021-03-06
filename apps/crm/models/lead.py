# Librerias Django
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias de terceros
from apps.base.models import PyFather, PyPartner

# Librerias en carpetas locales
from .stage import PyStage


class PyLead(PyFather):
    name = models.CharField('Nombre', max_length=80)
    partner_id = models.ForeignKey(PyPartner, null=True, blank=True, on_delete=models.CASCADE)
    user_id = models.ForeignKey('base.PyUser', null=True, blank=True, on_delete=models.CASCADE)
    stage_id = models.ForeignKey(PyStage, null=True, blank=True, on_delete=models.CASCADE)
    income = models.DecimalField('Ingreso', max_digits=10, decimal_places=2, default=0)

    content = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('crm:lead-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.name)

    def give_total_lead(self):
        return self.objects.count()

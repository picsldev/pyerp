from django.db import models
from django.urls import reverse
from .company import PyCompany


class BaseConfig(models.Model):

    online = models.BooleanField('Online', default=False)
    main_company_id = models.ForeignKey(PyCompany, on_delete='cascade', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('base-config', kwargs={'pk': self.pk})

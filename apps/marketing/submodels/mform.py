from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from .campaign import PyCampaign

class PyMform(models.Model):
    name = models.CharField('Nombre', max_length=255)
    campaign_id = models.ForeignKey(PyCampaign, null=True, blank=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('mform-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.name)
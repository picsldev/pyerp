# Librerias Django
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from ...base.submodels.father import PyFather


class PyApp(PyFather):
    name = models.CharField(_("Name"), max_length=80)
    author = models.CharField(_("Author"), max_length=80)
    description = models.TextField(_("description"), blank=True, null=True)
    installed = models.BooleanField(default=False, blank=True, null=True)


    def get_absolute_url(self):
        return reverse('lead-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.name)
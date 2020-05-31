# Librerias Django
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from .father import PyFather


class PyLog(PyFather):
    name = models.CharField('Nombre', max_length=40)
    note = models.TextField(blank=True, null=True)

    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)

    def get_absolute_url(self):
        return reverse('log-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_on']

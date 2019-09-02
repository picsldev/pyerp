# -*- coding: utf-8 -*-
# Part of PyERP. See LICENSE file for full copyright and licensing details.
from django.db import models
from .father import PyFather
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse


class PyCountry(PyFather):
    name = models.CharField(_("Name") ,max_length=40)

    def __str__(self):
        return format(self.name)

    def get_absolute_url(self):
        return reverse('country-detail', kwargs={'pk': self.pk})
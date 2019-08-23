from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from .father import PyFather

class PyProductWebCategory(PyFather):
    name = models.CharField(max_length=40)

    def __str__(self):
        return format(self.name)

    def get_absolute_url(self):
        return reverse('product-webcategory-detail', kwargs={'pk': self.pk})
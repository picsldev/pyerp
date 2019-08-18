from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Tabla de POS
class PyPos(models.Model):
    name = models.CharField('Nombre', max_length=80)


    def get_absolute_url(self):
        return reverse('pos-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.name)

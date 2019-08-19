from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import datetime

class PyPost(models.Model):
    name = models.CharField('Nombre', max_length=255)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.name)
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class PyPost(models.Model):
    name = models.CharField('Nombre', max_length=255)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.name)
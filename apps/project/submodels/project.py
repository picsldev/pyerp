from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


PROJECT_STATE = (
        ("nuevo", "Nuevo"),
        ('trabajando', 'Trabajando'),
        ('finalizado', 'Finalizado')
    )


class PyProject(models.Model):
    name = models.CharField('Nombre', max_length=80)
    note = models.TextField(blank=True, null=True)
    user_id = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    state = models.CharField(
        choices=PROJECT_STATE, max_length=64, default='nuevo')

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.name)
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

PROJECT_STATE = (
        ("nuevo", "Nuevo"),
        ('trabajando', 'Trabajando'),
        ('finalizado', 'Finalizado')
    )

class PyTask(models.Model):
    name = models.CharField('Nombre', max_length=80)
    note = models.TextField(blank=True, null=True)
    user_id = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    income = models.DecimalField('Ingreso', max_digits=10, decimal_places=2, default=0)

    state = models.CharField(
        choices=PROJECT_STATE, max_length=64, default='nuevo')

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.name)

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class PyAccountMove(models.Model):
    STATE = (
        ("draft", "Borrador"),
        ('posted', 'Validado'),
    )
    code = models.CharField('Código', max_length=80)
    name = models.CharField('Nombre', max_length=80)
    state = models.CharField(
        choices=STATE, max_length=64, default='draft')

    def get_absolute_url(self):
        return reverse('account-move-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '[%s] %s' % (self.code, self.name)


class PyAccountMoveLine(models.Model):
    name = models.CharField('Nombre', max_length=80)
    move = models.ForeignKey(to=PyAccountMove, on_delete='cascade', related_name='lines', null=True, blank=True)

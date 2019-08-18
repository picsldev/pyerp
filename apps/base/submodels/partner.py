from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class PyPartner(models.Model):
    name = models.CharField('Nombre', max_length=40)
    street = models.CharField('Calle', max_length=100, blank=True)
    street_2 = models.CharField('Calle 2', max_length=100, blank=True)
    city = models.CharField('Ciudad', max_length=50, blank=True)
    phone = models.CharField('Teléfono', max_length=20, blank=True)
    email = models.EmailField('Correo', max_length=40, blank=True)
    rut = models.CharField('RUT', max_length=12, blank=True)
    giro = models.CharField('Giro', max_length=80, blank=True)
    customer = models.BooleanField('Es cliente', default=True)
    provider = models.BooleanField('Es proveedor', default=True)
    for_invoice = models.BooleanField('Para Facturar', default=True)
    note = models.TextField(blank=True, null=True)

    created_by = models.ForeignKey(
        User, related_name='pypartner_created_by',
        on_delete=models.SET_NULL, null=True)

    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)

    def get_absolute_url(self):
        return reverse('partner-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s%s' % (self.rut and ('[%s] ' % self.rut) or '', self.name)

    def __repr__(self):
        return '%s%s' % (self.rut and ('[%s] ' % self.rut) or '', self.name)

    class Meta:
        ordering = ['-created_on']

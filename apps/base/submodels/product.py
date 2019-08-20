from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from .product_category import PyProductCategory
from .product_webcategory import PyProductWebCategory

PRODUCT_CHOICE = (
        ("product", "Almacenable"),
        ('consu', 'Consumible'),
        ('service', 'Servicio')
    )


# Tabla de Product
class PyProduct(models.Model):
    name = models.CharField('Nombre', max_length=80)
    code = models.CharField('Código', max_length=80, blank=True)
    bar_code = models.CharField('Cod. Barras', max_length=80, blank=True)
    price = models.DecimalField('Precio', max_digits=10, decimal_places=2, default=1)
    cost = models.DecimalField('Costo', max_digits=10, decimal_places=2, default=0)
    category_id = models.ForeignKey(PyProductCategory, null=True, blank=True, on_delete=models.CASCADE)
    web_category_id = models.ForeignKey(PyProductWebCategory, null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    web_active = models.BooleanField('Web', default=False)

    type = models.CharField(
        choices=PRODUCT_CHOICE, max_length=64, default='consu')

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})

    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)

    def __str__(self):
        return format(self.name)

    class Meta:
        ordering = ['created_on']
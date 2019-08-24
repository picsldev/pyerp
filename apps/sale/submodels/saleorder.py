from django.db import models
from ...base.submodels.father import PyFather
from ...base.models import PyPartner

SALE_STATE = (
        ("draft", "Borrador"),
        ('open', 'Consumible'),
        ('cancel', 'Servicio')
    )


# Tabla Sale Order
class PySaleOrder(PyFather):
    name = models.CharField('Nombre', max_length=80)
    partner_id = models.ForeignKey(PyPartner, null=True, blank=True, on_delete=models.CASCADE)
    date_order = models.DateTimeField(auto_now=True, blank=True, null=True)

    amount_untaxec = models.DecimalField('Monto Neto', max_digits=10, decimal_places=2)
    amount_taxt = models.DecimalField('Total Impuestos', max_digits=10, decimal_places=2)
    amount_total = models.DecimalField('Total', max_digits=10, decimal_places=2)

    description = models.TextField(blank=True, null=True)
    state = models.CharField(choices=SALE_STATE, max_length=64, default='draft')
from django.views.generic import ListView
from ..submodels.saleorder import PySaleOrder
from django.contrib.auth.mixins import LoginRequiredMixin


SALE_FIELDS = [
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Cliente', 'field': 'partner_id'},
            {'string': 'Estado', 'field': 'state'},
             ]

LEAD_FIELDS_SHORT = ['name','partner_id','state']


class SaleOrderListView(LoginRequiredMixin, ListView):
    model = PySaleOrder
    template_name = 'erp/list.html'
    login_url = "/erp/login"

    def get_context_data(self, **kwargs):
        context = super(SaleOrderListView, self).get_context_data(**kwargs)
        context['title'] = 'Orden de Venta'
        context['detail_url'] = 'sale-order-detail'
        context['add_url'] = 'sale-order-add'
        context['fields'] = SALE_FIELDS
        return context
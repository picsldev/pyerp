from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from ...base.models import PyPartner
from ..common import check_rut, validarRut

PARTNER_FIELDS = [
    {'string': 'RUT', 'field': 'rut'},
    {'string': 'Nombre / Razón Social', 'field': 'name'},
    {'string': 'Dirección', 'field': 'street'},
    {'string': 'Teléfono', 'field': 'phone'},
    {'string': 'Email', 'field': 'email'},
    {'string': 'Para Facturar', 'field': 'for_invoice'},
    {'string': 'Creado por', 'field': 'created_by'},
    {'string': 'Creado', 'field': 'created_on'},
    {'string': 'Notas', 'field': 'note'},
    {'string': 'Canal', 'field': 'channel_id'},
    {'string': 'Campaña', 'field': 'campaign_id'},
]

PARTNER_FIELDS_SHORT = ['rut', 'name', 'street', 'email', 'phone', 'note', 'customer', 'provider', 'channel_id', 'campaign_id', 'for_invoice']


class CustomerListView(ListView):
    model = PyPartner
    template_name = 'erp/list.html'
    queryset = PyPartner.objects.filter(customer=True).all()

    def get_context_data(self, **kwargs):
        context = super(CustomerListView, self).get_context_data(**kwargs)
        context['title'] = 'Partners'
        context['detail_url'] = 'partner-detail'
        context['add_url'] = 'partner-add'
        context['fields'] = PARTNER_FIELDS
        return context


class ProviderListView(ListView):
    model = PyPartner
    template_name = 'erp/list.html'
    queryset = PyPartner.objects.filter(provider=True).all()

    def get_context_data(self, **kwargs):
        context = super(ProviderListView, self).get_context_data(**kwargs)
        context['title'] = 'Partners'
        context['detail_url'] = 'partner-detail'
        context['add_url'] = 'partner-add'
        context['fields'] = PARTNER_FIELDS
        return context


class PartnerDetailView(DetailView):
    model = PyPartner
    template_name = 'erp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(PartnerDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'partners', 'name': 'Partners'}]
        context['update_url'] = 'partner-update'
        context['delete_url'] = 'partner-delete'
        context['fields'] = PARTNER_FIELDS
        return context


class PartnerCreateView(CreateView):
    model = PyPartner
    fields = ['name', 'email', 'phone', 'rut', 'customer', 'provider']
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(PartnerCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear partner'
        context['breadcrumbs'] = [{'url': 'partners', 'name': 'Partners'}]
        context['back_url'] = reverse('partners')
        return context

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super(PartnerCreateView, self).get_form(form_class)
        form.fields['rut'].widget.attrs = {'placeholder': '00.000.000-0'}
        return form


class PartnerUpdateView(UpdateView):
    model = PyPartner
    fields = PARTNER_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(PartnerUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'partners', 'name': 'Partners'}]
        context['back_url'] = reverse('partner-detail', kwargs={'pk': context['object'].pk})
        return context

    def form_valid(self, form):
        rut = form.data.get('rut')
        if validarRut(rut):
            self.object.rut = check_rut(rut, 1)
        else:
            form.add_error('rut', 'Formato de RUT inválido')
            return self.form_invalid(form)
        return super(PartnerUpdateView, self).form_valid(form)

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super(PartnerUpdateView, self).get_form(form_class)
        form.fields['rut'].widget.attrs = {'placeholder': '00.000.000-0'}
        return form


@login_required(login_url="/erp/login")
def DeletePartner(self, pk):
    partner = PyPartner.objects.get(id=pk)
    partner.delete()
    return redirect(reverse('partners'))

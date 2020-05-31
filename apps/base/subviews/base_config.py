from django.views.generic.edit import UpdateView
from ..models import BaseConfig


class UpdateBaseConfigView(UpdateView):
    model = BaseConfig
    template_name = 'erp/form.html'
    fields = ['online', 'open_menu','main_company_id']

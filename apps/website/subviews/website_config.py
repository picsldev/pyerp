from django.views.generic.edit import UpdateView
from ..submodels.website_config import WebsiteConfig
from django.shortcuts import render


class UpdateWebsiteConfigView(UpdateView):
    model = WebsiteConfig
    template_name = 'erp/form.html'
    fields = ['show_blog', 'show_shop', 'under_construction']
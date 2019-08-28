from django.db import models
from django.urls import reverse
from ...base.submodels.father import PyFather



class WebsiteConfig(PyFather):
    show_blog = models.BooleanField('Mostrar Blog', default=False)
    show_shop = models.BooleanField('Mostrar Tienda', default=False)
    show_chat = models.BooleanField('Mostrar Chat', default=False)
    under_construction = models.BooleanField('En Construcción', default=False)


    def get_absolute_url(self):
        return reverse('website-config', kwargs={'pk': self.pk})
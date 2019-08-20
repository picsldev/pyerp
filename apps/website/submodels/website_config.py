from django.db import models
from django.urls import reverse


class WebsiteConfig(models.Model):
    show_blog = models.BooleanField('Mostrar Blog', default=False)
    show_shop = models.BooleanField('Mostrar Tienda', default=False)
    under_construction = models.BooleanField('En Construcción', default=False)


    def get_absolute_url(self):
        return reverse('website-config', kwargs={'pk': self.pk})
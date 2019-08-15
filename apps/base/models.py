from django.db import models
from django.urls import reverse


class PyCountry(models.Model):
    name = models.CharField(max_length=40)


class PyRegion(models.Model):
    name = models.CharField(max_length=40)


class PyComuna(models.Model):
    name = models.CharField(max_length=40)


class PyCompany(models.Model):
    name = models.CharField(max_length=40)
    street = models.CharField(max_length=100, blank=True)
    street_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=40, blank=True)
    rut = models.CharField(max_length=12, blank=True)
    giro = models.CharField(max_length=80, blank=True)

    country_id = models.ForeignKey(PyCountry, null=True, blank=True, on_delete=models.CASCADE)
    region_id = models.ForeignKey(PyRegion, null=True, blank=True, on_delete=models.CASCADE)
    comuna_id = models.ForeignKey(PyComuna, null=True, blank=True, on_delete=models.CASCADE)


class PyPartner(models.Model):
    name = models.CharField(max_length=40)
    street = models.CharField(max_length=100, blank=True)
    street_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=40, blank=True)
    rut = models.CharField(max_length=12, blank=True)
    giro = models.CharField(max_length=80, blank=True)

    def get_absolute_url(self):
        return reverse('partner-detail', kwargs={'pk': self.pk})

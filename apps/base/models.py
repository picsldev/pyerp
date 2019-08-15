from django.db import models

class PyCountry(models.Model):
    name = models.CharField(max_length=40)


class PyRegion(models.Model):
    name = models.CharField(max_length=40)

class PyComuna(models.Model):
    name = models.CharField(max_length=40)


class PyCompany(models.Model):
    name = models.CharField(max_length=40)
    street = models.CharField(max_length=100)
    street_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    rut = models.CharField(max_length=12)
    giro = models.CharField(max_length=80)

    country_id = models.ForeignKey(PyCountry, null=True, blank=True, on_delete=models.CASCADE)
    region_id = models.ForeignKey(PyRegion, null=True, blank=True, on_delete=models.CASCADE)
    comuna_id = models.ForeignKey(PyComuna, null=True, blank=True, on_delete=models.CASCADE)


class PyPartner(models.Model):
    name = models.CharField(max_length=40)
    street = models.CharFild(max_length=100)
    street_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    rut = models.CharField(max_length=12)
    giro = models.CharField(max_length=80)


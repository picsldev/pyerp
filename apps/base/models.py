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

    def get_absolute_url(self):
        return reverse('company-detail', kwargs={'pk': self.pk})

# Tabla de Partner
class PyPartner(models.Model):
    name = models.CharField('Nombre', max_length=40)
    street = models.CharField('Calle', max_length=100, blank=True)
    street_2 = models.CharField('Calle 2', max_length=100, blank=True)
    city = models.CharField('Ciudad', max_length=50, blank=True)
    phone = models.CharField('Teléfono', max_length=20, blank=True)
    email = models.CharField('Correo', max_length=40, blank=True)
    rut = models.CharField('RUT', max_length=12, blank=True)
    giro = models.CharField('Giro', max_length=80, blank=True)
    customer = models.BooleanField('Es cliente', default=False)
    provider = models.BooleanField('Es proveedor', default=False)

    def get_absolute_url(self):
        return reverse('partner-detail', kwargs={'pk': self.pk})

# Tabla de Product
class PyProduct(models.Model):
    name = models.CharField('Nombre', max_length=80)
    code = models.CharField('Código', max_length=80, blank=True)
    bar_code = models.CharField('Cod. Barras', max_length=80, blank=True)
    price = models.DecimalField('Precio', max_digits=10, decimal_places=2, default=1)
    cost = models.DecimalField('Costo', max_digits=10, decimal_places=2, default=0)

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})



# Tabla de Product
class PyEmployee(models.Model):
    name = models.CharField('Nombre', max_length=80)
    name2 = models.CharField('Segundo Nombre', max_length=80, blank=True)
    first_name = models.CharField('Apellido Paterno', max_length=80, blank=True)
    last_name = models.CharField('Apellido Materno', max_length=80, blank=True)
    phone = models.CharField('Teléfono', max_length=20, blank=True)
    email = models.CharField('Correo', max_length=40, blank=True)

    def get_absolute_url(self):
        return reverse('employee-detail', kwargs={'pk': self.pk})

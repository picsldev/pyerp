from django.db import models


class PyCountry(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return format(self.name)


class PyRegion(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return format(self.name)


class PyComuna(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return format(self.name)

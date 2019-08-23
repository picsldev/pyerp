from django.db import models
from .father import PyFather


class PyCountry(PyFather):
    name = models.CharField(max_length=40)

    def __str__(self):
        return format(self.name)


class PyRegion(PyFather):
    name = models.CharField(max_length=40)

    def __str__(self):
        return format(self.name)


class PyComuna(PyFather):
    name = models.CharField(max_length=40)

    def __str__(self):
        return format(self.name)

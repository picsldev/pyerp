# Librerias Django
from django.contrib.auth.models import User
from django.db import models


class PyFather(models.Model):
    active = models.BooleanField(default=True, blank=True, null=True)
    fc = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    fm = models.DateTimeField(auto_now=True, blank=True, null=True)
    # uc = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    uc = models.IntegerField(null=True, blank=True)
    um = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True

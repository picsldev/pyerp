from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from .submodels.employee import PyEmployee
from .submodels.department import PyDepartment

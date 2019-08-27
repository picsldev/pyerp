from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from .submodels.partner import PyPartner
from .submodels.base_config import BaseConfig
from .submodels.company import PyCompany
from .submodels.locations import PyComuna, PyCountry, PyRegion

from .submodels.product import PyProduct
from .submodels.product_category import PyProductCategory
from .submodels.product_webcategory import PyProductWebCategory
from .submodels.log import PyLog
from .submodels.cron import PyCron
from .submodels.currency import PyCurrency

from datetime import datetime, timedelta
from django.utils.timesince import timesince
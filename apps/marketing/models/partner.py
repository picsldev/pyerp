from django.db import models

from ...base.submodels.partner import PyPartner
from .campaign import PyCampaign
from .channel import PyChannel


class MarketingPartner(PyPartner):
    class Meta:
        app_label = 'base'

    channel_id = models.ForeignKey(PyChannel, null=True, blank=True, on_delete=models.CASCADE)
    campaign_id = models.ForeignKey(PyCampaign, null=True, blank=True, on_delete=models.CASCADE)

from django.db import models
from Enso.app.models.zipcode import Zipcode
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from datetime import datetime

CENTRETYPE = (
    ('MK', _('Market')),
    ('HC', _('Hawker')),
    ('MHC', _('Market & Hawker'))
)

class HawkerCentre(models.Model):

    centre_name = models.TextField(null=False,blank=False)
    centre_type = models.CharField(max_length=3,choices= CENTRETYPE,default='HC')
    zip_code = models.ForeignKey(Zipcode, null=True,blank=True, related_name='hawker_centre',on_delete=models.CASCADE)
    
    def get_centre_type(self):
        return self.get_centre_type_display()

    class Meta:
        app_label = "Enso"

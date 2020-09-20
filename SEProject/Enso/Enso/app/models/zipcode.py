from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

class Zipcode(models.Model):
    zipcode = models.CharField(max_length=6, primary_key=True)
    latitude = models.FloatField(default=1.2789,null=False, blank=False)
    longitude = models.FloatField(default=103.8536,null=False, blank=False)
    address = models.TextField(default="TEMP",null=False,blank=False)

    class Meta:
        app_label = "Enso"

    def getFormattedAddress(self):
        return self.address + ", S(" + self.zipcode + ")"

from django.db import models
from django.db.models.query_utils import Q
from Enso.app.models.food_store import FoodStore
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from datetime import datetime,date
from Enso.app.controllers.logic.cloudinary import getImageURL

STATUS = (
  ('P', _("Pending")),
  ('F', _("Full")),
  ('C', _("Completed")),
)


class Gathering(models.Model):

    name = models.TextField(default="Gathering", null=False,blank=False)
    food_store = models.ForeignKey(FoodStore, null=True,blank=True, related_name='gathering',on_delete=models.CASCADE)
    date = models.DateField(_("Date"),default=date.today)
    start_time = models.TimeField()
    no_pax = models.IntegerField(null=True,blank=True)
    chat_id = models.TextField(null=True,blank=True)
    status = models.CharField(max_length=1,choices= STATUS,default='P')
    receipt = models.TextField(default="receipt-default-pic", null=True, blank=True)

    class Meta:
        app_label = "Enso"

    def getRemainingPax(self):
        return self.no_pax - self.getCurrentPax()

    def getCurrentPax(self):
        gatherings = Gathering.objects.all()
        return len(gatherings.filter(Q(user_gathering__gathering = self.id) & Q(user_gathering__status='J')))

    def getPendingSelected(self,status):
        gatherings = Gathering.objects.all()
        num_requests = len(gatherings.filter(Q(user_gathering__gathering = self.id) & Q(user_gathering__status = status)))
        return num_requests

    def getPendingInvites(self):
        return self.getPendingSelected("I")

    def getPendingRequests(self):
        return self.getPendingSelected("R")

    def get_receipt_url(self):
        return getImageURL(self.receipt,'jpg')

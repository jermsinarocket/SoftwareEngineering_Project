from django.db import models
from Enso.app.models.food_store import FoodStore
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from datetime import datetime,date

class Gathering(models.Model):

    name = models.TextField(default="Gathering", null=False,blank=False)
    food_store = models.ForeignKey(FoodStore, null=True,blank=True, related_name='gathering',on_delete=models.CASCADE)
    date = models.DateField(_("Date"),default=date.today)
    start_time = models.TimeField()
    no_pax = models.IntegerField(null=True,blank=True)
    chat_id = models.TextField(null=True,blank=True)

    class Meta:
        app_label = "Enso"

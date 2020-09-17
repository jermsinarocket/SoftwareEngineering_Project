from django.db import models
from Enso.app.models.food_store import FoodStore
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from datetime import datetime

WEEKDAYS = [
  (1, _("Monday")),
  (2, _("Tuesday")),
  (3, _("Wednesday")),
  (4, _("Thursday")),
  (5, _("Friday")),
  (6, _("Saturday")),
  (7, _("Sunday")),
]

class OpeningHours(models.Model):

    food_store = models.ForeignKey(FoodStore, null=True,blank=True, related_name='opening_hours',on_delete=models.CASCADE)
    weekday = models.IntegerField(choices=WEEKDAYS)
    from_hour = models.TimeField()
    to_hour = models.TimeField()

    class Meta:
        app_label = "Enso"
        ordering = ('weekday','from_hour')

    def __unicode__(self):
        return u'%s: %s - %s' % (self.get_weekday_display(),
                                 self.from_hour, self.to_hour)

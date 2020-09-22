from django.db import models
from Enso.app.models.profile import Profile
from Enso.app.models.food_store import FoodStore
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from datetime import datetime

class Rating(models.Model):
    user_profile = models.ForeignKey('Profile', related_name='rating', on_delete=models.CASCADE, null=True)
    food_store  = models.ForeignKey('FoodStore', related_name='rating', on_delete=models.CASCADE, null=True)
    rating = models.IntegerField(default=1,null=False, blank=False)

    class Meta:
        app_label = "Enso"

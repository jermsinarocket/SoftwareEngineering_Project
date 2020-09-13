from django.db import models
from Enso.app.models.profile import Profile
from Enso.app.models.food_category import FoodCategory
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from datetime import datetime


class FoodPreferences(models.Model):
    user_profile = models.ForeignKey('Profile', related_name='food_preferences', on_delete=models.CASCADE, null=True)
    food_category  = models.ForeignKey('FoodCategory', related_name='food_preferences', on_delete=models.CASCADE, null=True)

    class Meta:
        app_label = "Enso"

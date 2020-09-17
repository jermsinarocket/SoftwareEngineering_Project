from django.db import models
from Enso.app.models.profile import Profile
from Enso.app.models.gathering import Gathering
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from datetime import datetime


class UserGathering(models.Model):
    user_profile = models.ForeignKey('Profile', related_name='user_gathering', on_delete=models.CASCADE, null=True)
    gathering  = models.ForeignKey('Gathering', related_name='user_gathering', on_delete=models.CASCADE, null=True)

    class Meta:
        app_label = "Enso"

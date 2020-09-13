from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

class LevelSystem(models.Model):
    min_points = models.IntegerField(default=1,null=False, blank=False)
    max_points = models.IntegerField(default=1,null=False, blank=False)

    class Meta:
        app_label = "Enso"

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from datetime import datetime

class FoodCategory(models.Model):
    category_name = models.TextField(default="Cuisine",blank=True,null=True)

    class Meta:
        app_label = "Enso"

    def getCategoryFormatted(self):
        return self.category_name + ' Cuisine'

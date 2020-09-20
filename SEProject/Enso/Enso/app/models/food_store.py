from django.db import models
from Enso.app.models.hawker_centre import HawkerCentre
from Enso.app.models.food_category import FoodCategory
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
import cloudinary
import cloudinary.uploader
import cloudinary.api

class FoodStore(models.Model):

    store_name = models.TextField(null=False,blank=False)
    unit_number = models.TextField(null=False,blank=False)
    hawker_centre = models.ForeignKey(HawkerCentre, null=True,blank=True, related_name='food_store',on_delete=models.CASCADE)
    store_image = models.TextField(default="store-default-pic", null=True, blank=True)
    store_menu = models.TextField(null=True, blank=True)
    cuisine_type = models.ForeignKey(FoodCategory, null=True,blank=True, related_name='food_store',on_delete=models.CASCADE)
    cashless_payment = models.BooleanField(default=False)

    class Meta:
        app_label = "Enso"

    def get_storepic_url(self):
        return cloudinary.utils.cloudinary_url("Food Stores/" + self.store_image + ".jpg",secure=True)[0]

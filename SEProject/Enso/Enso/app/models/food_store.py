from django.db import models
from Enso.app.models.hawker_centre import HawkerCentre
from Enso.app.models.food_category import FoodCategory
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from Enso.app.controllers.logic.store_management import averageRatingCalculator,openingDays,openingHours
from Enso.app.controllers.logic.cloudinary import getImageURL,getImageList
import json

class FoodStore(models.Model):

    store_name = models.TextField(null=False,blank=False)
    unit_number = models.TextField(null=False,blank=False)
    hawker_centre = models.ForeignKey(HawkerCentre, null=True,blank=True, related_name='food_store',on_delete=models.CASCADE)
    store_image = models.TextField(default="store-default-pic", null=True, blank=True)
    store_menu = models.TextField(null=True, blank=True)
    cuisine_type = models.ForeignKey(FoodCategory, null=True,blank=True, related_name='food_store',on_delete=models.CASCADE)
    cashless_payment = models.BooleanField(default=False)
    store_rating = models.ManyToManyField('Profile', through='Rating', related_name='food_store')

    class Meta:
        app_label = "Enso"

    def get_storepic_url(self):
        return getImageURL(self.store_image,"jpg","Food Stores/store-" + str(self.id) + "/")

    def get_store_menu(self):
        return getImageURL(self.store_menu,"pdf","Food Stores/store-" + str(self.id) + "/")

    def get_store_pics(self):
        return getImageList(self.id)

    def get_average_rating(self):
        return averageRatingCalculator(self.id)[1]

    def get_total_num_reviews(self):
        return averageRatingCalculator(self.id)[0]

    def get_operating_days(self):
        return openingDays(self.id)

    def get_operating_hours(self):
        print(openingHours(self.id))
        return openingHours(self.id)

    def get_store_name(self):
        return self.store_name

from django.db import models
from django.contrib.auth.models import User
from Enso.app.models.food_category import FoodCategory
from Enso.app.models.gathering import Gathering
from Enso.app.models.level_system import LevelSystem
from Enso.app.models.zipcode import Zipcode
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from datetime import datetime

from Enso.app.controllers.logic.cloudinary import getImageURL

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    food_categories = models.ManyToManyField('FoodCategory', through='FoodPreferences', related_name='user_profile')
    gatherings = models.ManyToManyField('Gathering', through='UserGathering', related_name='user_profile')
    current_level = models.ForeignKey(LevelSystem, default=1,related_name='user_profile',on_delete=models.CASCADE )
    zip_code = models.ForeignKey(Zipcode, null=True,blank=True, related_name='user_profile',on_delete=models.SET_NULL)
    points = models.IntegerField(default=0,null=False, blank=False)
    gender = models.CharField(default='Male',max_length=10, blank=False)
    first_name = models.TextField(default="John",blank=False)
    last_name = models.TextField(blank=True,null=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    phone_number = models.CharField(max_length=8,blank=True,null=True)
    profile_pic = models.TextField(default="user-default-profile-pic", null=False, blank=False)

    class Meta:
        app_label = "Enso"

    def get_gender(self):
        return self.gender

    def get_date_joined(self):
        return self.date_joined.strftime('%d-%m-%Y')

    def get_full_name(self):
        return self.last_name + ' ' + self.first_name

    def get_profile_url(self):
        return getImageURL(self.profile_pic,'jpg')
    
    def get_user(self):
        return self.user

    def get_level_id(self):
        return self.current_level.id

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

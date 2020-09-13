from django.db import models
from django.contrib.auth.models import User
from Enso.app.models.food_category import FoodCategory
from Enso.app.models.level_system import LevelSystem
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
import cloudinary
import cloudinary.uploader
import cloudinary.api
from datetime import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='user_profile')
    food_categories = models.ManyToManyField('FoodCategory', through='FoodPreferences', related_name='user_profile')
    current_level = models.ForeignKey(LevelSystem, default=1, on_delete=models.CASCADE, related_name='user_profile')
    points = models.IntegerField(default=0,null=False, blank=False)
    gender = models.CharField(default='Male',max_length=10, blank=False)
    first_name = models.TextField(default="John",blank=False)
    last_name = models.TextField(blank=True,null=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    profile_pic = models.TextField(default="user-default-profile-pic", null=False, blank=False)

    class Meta:
        app_label = "Enso"

    def get_gender(self):
        return self.gender

    def get_birth_date(self):
        return self.birth_date.strftime('%d-%m-%Y')

    def get_date_joined(self):
        return self.date_joined.strftime('%d-%m-%Y')

    def get_full_name(self):
        return self.last_name + ' ' + self.first_name

    def get_profile_url(self):
        return cloudinary.utils.cloudinary_url("profile_pic_user"+ str(self.id) + ".jpg")

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

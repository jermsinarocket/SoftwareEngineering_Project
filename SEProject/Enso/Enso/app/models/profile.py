from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from datetime import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(default='M',max_length=1, blank=False)
    birth_date = models.DateField(null=True, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    avatar = models.ImageField(upload_to='Enso/static/images', null=True, blank=True)

    class Meta:
        app_label = "Enso"
        
    def get_gender(self):
        return self.gender

    def get_birth_date(self):
        return self.birth_date

    def get_date_joined(self):
        return self.date_joined.strftime('%d-%m-%Y')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

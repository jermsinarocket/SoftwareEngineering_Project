from django.db import models
from Enso.app.models.profile import Profile
from Enso.app.models.gathering import Gathering
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from datetime import datetime

STATUS = (
    ('R', _("Requested")),
    ('I', _("Invited")),
    ('J', _("Joined"))
)

TYPE = (
    ('H', _("Host")),
    ('M', _("Member")),
)

class UserGathering(models.Model):

    user_profile = models.ForeignKey('Profile', related_name='user_gathering', on_delete=models.CASCADE, null=True)
    gathering  = models.ForeignKey('Gathering', related_name='user_gathering', on_delete=models.CASCADE, null=True)
    member_type =  models.CharField(max_length=1,choices= TYPE,default='M')
    status =  models.CharField(max_length=1,choices= STATUS,default='J')

    class Meta:
        app_label = "Enso"
        ordering = ['member_type']

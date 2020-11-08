from django.db.models.query_utils import Q
from Enso.app.models.profile import Profile
from Enso.app.models.level_system import LevelSystem
import os
import sys

def calculateLevel(user,points):
    user.points = user.points + points

    if(user.points  > user.current_level.max_points):
        user.current_level = LevelSystem.objects.get(id = user.current_level.id + 1)

    user.save()

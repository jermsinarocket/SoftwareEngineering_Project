from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.conf import settings
from django.template import loader
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
from django.core import serializers
from django.http import JsonResponse,QueryDict
from django.forms.models import model_to_dict
from Enso.app.models.gathering import Gathering
from Enso.app.models.user_gathering import UserGathering
from Enso.app.models.food_store import FoodStore
import os
import sys
import datetime

@login_required
def create_gathering(request):
    postData = request.POST

    gathering = Gathering.objects.create(name=postData['gathering_name'],
                                         start_time = postData['gathering_time'],
                                         date=datetime.datetime.strptime(postData['gathering_date'], "%d/%m/%Y").strftime("%Y-%m-%d"),
                                         no_pax=postData['no_pax'],
                                         food_store = FoodStore.objects.get(id = postData['store_id']))
    UserGathering.objects.create(user_profile = request.user.profile, gathering = gathering,member_type = 'H')
    return JsonResponse({"gathering_id":gathering.id})


@login_required
def create_chat(request):
    gathering = Gathering.objects.get(pk=request.POST['gathering_id'])
    gathering.chat_id = request.POST['group_id']
    gathering.save()
    return JsonResponse({'success':'true'})

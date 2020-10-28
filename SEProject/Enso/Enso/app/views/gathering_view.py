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
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from Enso.app.controllers.logic.gathering_manager import  host_get_pending_requests_count,participant_get_pending_requests_count
import os
import sys
import datetime
import json

@login_required
def gathering_page(request):
    return render(request,'gatheringpage.html',{"host_all_request":host_get_pending_requests_count(request.user,"I") + host_get_pending_requests_count(request.user,"R"),
                                                "participant_pending_request": participant_get_pending_requests_count(request.user)
                                                }
                )

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


@login_required
def load_existing_gatherings(request):

    gathering_ids = []
    now = datetime.datetime.now()
    gatherings = Gathering.objects.filter(Q(food_store= request.POST['store_id']) & Q(status='P') & ~Q(user_gathering__user_profile__id = request.user.profile.id) & ((Q(date=now.date())& Q(start_time__gte=now.time())) | Q(date__gte=now.date())))
    for gathering in gatherings:
        gathering_ids.append(gathering.id)
    return JsonResponse({'gathering_ids':gathering_ids})


@login_required
def request_join_gathering(request):
    gathering = Gathering.objects.get(id=request.POST['gathering_id'])
    UserGathering.objects.create(user_profile=request.user.profile,gathering = gathering,member_type='M',status='R')
    host_qdict = UserGathering.objects.filter(Q(gathering__id = request.POST['gathering_id']) & Q(member_type='H')).values('user_profile')
    for host in host_qdict:
        host_id = host['user_profile']
    return JsonResponse({'host_id':host_id,'gathering_name':gathering.name})

@login_required
@csrf_exempt
def delete_gathering(request):
    gathering_id = request.POST['gathering_id']
    UserGathering.objects.filter(gathering=gathering_id).delete()
    gathering_obj = Gathering.objects.filter(id=gathering_id)
    chat_id = gathering_obj.values('chat_id')[0]['chat_id']
    gathering_obj.delete()
    return JsonResponse({'chat_id':chat_id})

@login_required
@csrf_exempt
def update_pax(request):
    gathering = Gathering.objects.get(id=request.POST['gathering_id'])
    gathering.no_pax = request.POST['num_pax']
    gathering.save()
    return JsonResponse({'success':True})

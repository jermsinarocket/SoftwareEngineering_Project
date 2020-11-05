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
from Enso.app.models.profile import Profile
from Enso.app.models.user_gathering import UserGathering
from Enso.app.models.food_store import FoodStore
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from Enso.app.controllers.logic.gathering_manager import  host_get_pending_requests_count,participant_get_pending_requests_count,participant_get_pending_invites_count
from Enso.app.controllers.logic.level_system_manager import calculateLevel
from Enso.app.controllers.logic.cloudinary import uploadFile

import os
import sys
import datetime
import json

@login_required
def gathering_page(request):
    return render(request,'gatheringpage.html',{"host_all_request":host_get_pending_requests_count(request.user,"I") + host_get_pending_requests_count(request.user,"R"),
                                                "participant_pending_request": participant_get_pending_requests_count(request.user),
                                                "participant_pending_invite": participant_get_pending_invites_count(request.user),
                                                "all_users": Profile.objects.all()
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

@login_required
@csrf_exempt
def remove_member(request):
    gathering_id = request.POST['gathering_id']
    UserGathering.objects.filter(Q(gathering=gathering_id) & Q(user_profile=request.POST['user_id'])).delete()
    gathering_obj = Gathering.objects.filter(id=gathering_id)
    chat_id = gathering_obj.values('chat_id')[0]['chat_id']
    return JsonResponse({'chat_id':chat_id})

@login_required
@csrf_exempt
def invite_member(request):
    gathering = Gathering.objects.get(id=request.POST['gathering_id'])
    user_profile = Profile.objects.get(id=request.POST['user_id'])
    UserGathering.objects.create(user_profile=user_profile,gathering = gathering,member_type='M',status='I')
    return JsonResponse({'success':True})


@login_required
@csrf_exempt
def cancel_member(request):
    UserGathering.objects.filter(Q(gathering=request.POST['gathering_id']) & Q(user_profile=request.POST['user_id'])).delete()
    return JsonResponse({'success':True})

@login_required
@csrf_exempt
def approve_member(request):
    user_obj = UserGathering.objects.get(id= request.POST['user_id'])
    user_obj.status = "J"
    user_obj.save()
    return JsonResponse({'chat_id':user_obj.gathering.chat_id,'gathering_name':user_obj.gathering.name,'remove_id':user_obj.user_profile.id})


@login_required
@csrf_exempt
def leave_gathering(request):
    user_obj = UserGathering.objects.get(id= request.POST['user_gathering_id'])
    chat_id = user_obj.gathering.chat_id
    user_obj.delete()
    return JsonResponse({'chat_id':user_obj.gathering.chat_id})

@login_required
@csrf_exempt
def complete_gathering(request):
    post_data = request.POST
    confirmed_participants = post_data['confirmed_participants'].split(',')
    absent_participants = post_data['absent_participants'].split(',')
    print(absent_participants)
    gathering_id = post_data['gathering_id']

    for user_id in confirmed_participants:
         user_gathering = UserGathering.objects.get(id = int(user_id))
         calculateLevel(user_gathering.user_profile)

    for user_id in absent_participants:
        if(user_id != ''):
            UserGathering.objects.get(id = int(user_id)).delete()

    receipt_file_name = "receipt-" + str(gathering_id)
    gathering_obj = Gathering.objects.get(id = gathering_id)
    gathering_obj.receipt = receipt_file_name
    gathering_obj.status = 'C'
    gathering_obj.save()

    UserGathering.objects.filter(Q(gathering_id = gathering_id) & (Q(status = 'R') | Q(status = 'I'))).delete()

    uploadFile(request.FILES['file'],receipt_file_name)

    return JsonResponse({'chat_id':gathering_obj.chat_id})

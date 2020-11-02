from django.db.models.query_utils import Q
from django.db.models import Count
from django.http import JsonResponse,QueryDict
from django.forms.models import model_to_dict
from Enso.app.models.gathering import Gathering
from Enso.app.models.user_gathering import UserGathering
from django.forms.models import model_to_dict
import os
import sys
import datetime


def host_get_pending_requests_count(user,user_status):
    hosted_gatherings = UserGathering.objects.filter(Q(user_profile = user.profile) & Q(member_type='H')).values("gathering_id")
    hosted_gatherings_id = []

    for gathering in hosted_gatherings:
        hosted_gatherings_id.append(gathering['gathering_id'])

    user_requests = UserGathering.objects.filter(Q(gathering_id__in=hosted_gatherings_id) & Q(member_type='M') & Q(status=user_status))
    return len(user_requests)

def participant_get_pending_requests_count(user):
    user_requests = UserGathering.objects.filter(Q(user_profile = user.profile) & Q(member_type='M') & Q(status="R"))
    return len(user_requests)

def participant_get_pending_invites_count(user):
    user_requests = UserGathering.objects.filter(Q(user_profile = user.profile) & Q(member_type='M') & Q(status="I"))
    return len(user_requests)

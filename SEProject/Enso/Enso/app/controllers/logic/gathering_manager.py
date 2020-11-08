from django.db.models.query_utils import Q
from django.db.models import Count
from django.http import JsonResponse,QueryDict
from django.forms.models import model_to_dict
from Enso.app.models.gathering import Gathering
from Enso.app.models.user_gathering import UserGathering
from django.forms.models import model_to_dict
from datetime import date,datetime
import os
import sys


def host_get_upcoming(user):
    hosted_gatherings = filter_all_upcoming(UserGathering.objects.filter((Q(user_profile = user.profile) & Q(member_type='H'))))
    hosted_gatherings_id = []

    for gathering in hosted_gatherings.values("gathering_id"):
        hosted_gatherings_id.append(gathering['gathering_id'])

    user_requests = UserGathering.objects.filter(Q(gathering_id__in=hosted_gatherings_id) & Q(member_type='M') & (Q(status='I') | Q(status='R')))
    return hosted_gatherings,len(user_requests)

def participant_get_pending_requests(user):
    user_requests = filter_all_upcoming(UserGathering.objects.filter(Q(user_profile = user.profile) & Q(member_type='M') & Q(status="R")))
    return user_requests

def participant_get_pending_invites(user):
    user_invites = filter_all_upcoming(UserGathering.objects.filter(Q(user_profile = user.profile) & Q(member_type='M') & Q(status="I")))
    return user_invites

def upcoming_gatherings(user):
    return filter_all_upcoming(UserGathering.objects.filter((Q(user_profile = user.profile) & Q(status="J")))).order_by('gathering__date')

def participant_joined_gatherings(user):
    return filter_all_upcoming(UserGathering.objects.filter((Q(user_profile = user.profile) & Q(status="J") &Q(member_type='M')))).order_by('gathering__date')

def pending_complete_gatherings(user):
    return UserGathering.objects.filter((Q(user_profile = user.profile) & Q(status="J") & Q(gathering__status = "P")) & (Q(gathering__date__lt=date.today()) | (Q(gathering__date=date.today()) & Q(gathering__start_time__lt=datetime.now().time().strftime("%X"))))).order_by('gathering__date')

def completed_gatherings(user):
    return UserGathering.objects.filter(Q(user_profile = user.profile) & Q(gathering__status = "C")).order_by('gathering__start_time')

def get_reviews(user):
    return UserGathering.objects.filter(Q(user_profile = user.profile) & Q(status="J") & Q(rating__isnull = True) & Q(gathering__status="C"))

def filter_all_upcoming(usergathering_obj):
    return usergathering_obj.filter(Q(gathering__status = 'P') & (Q(gathering__date__gt=date.today()) | (Q(gathering__date=date.today()) & Q(gathering__start_time__gt=datetime.now().time().strftime("%X")))))

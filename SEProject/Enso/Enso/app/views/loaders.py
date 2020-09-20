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
from django.core.mail import send_mail
from Enso.app.models.profile import Profile
from Enso.app.models.food_category import FoodCategory
from Enso.app.models.food_preferences import FoodPreferences
from Enso.app.models.food_store import FoodStore
from Enso.app.models.zipcode import Zipcode
from Enso.app.models.hawker_centre import HawkerCentre
from Enso.app.controllers.distance_routing import route
import os
import sys
import requests
from django.core import serializers
from django.http import JsonResponse,QueryDict

@login_required
def loadFoodListings(request):
    if request.method == 'POST':
        post_data = request.POST
        curr_lat = post_data['curr_lat']
        curr_long = post_data['curr_long']

        stores_qdict = FoodStore.objects.all()

        if('store_search' in post_data):
            store_search = post_data['store_search']
            #stores = stores.filter(store_name__icontains = post_data['store_search'])
            stores_qdict = stores_qdict.filter(Q(hawker_centre__centre_name__icontains = post_data['store_search']) | Q(store_name__icontains = post_data['store_search']))

        if('food_cats' in post_data):
            filt_food_cats = post_data['food_cats'].split(',')
            stores_qdict = stores_qdict.filter(cuisine_type__in=[int(x) for x in filt_food_cats])

        stores_list = []

        if(len(stores_qdict) != 0):
            stores_list = route(stores_qdict,curr_lat,curr_long)

        return JsonResponse({'stores':stores_list})

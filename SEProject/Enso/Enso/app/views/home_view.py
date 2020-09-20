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
from Enso.app.models.zipcode import Zipcode
from Enso.app.models.hawker_centre import HawkerCentre

import os
import sys
import requests

import cloudinary
import cloudinary.uploader
import cloudinary.api

@login_required
def homepage(request):

    userProfile = Profile.objects.get(user_id= request.user.id)
    food_categories = FoodCategory.objects.all()
    #r = requests.get("http://res.cloudinary.com/hgdcwue1c/image/list/test.json")

    '''
    r = requests.get(url = "https://data.gov.sg/api/action/datastore_search?resource_id=8f6bba57-19fc-4f36-8dcf-c0bda382364d")
    results = r.json()['result']['records']

    for item in results:
        name_of_centre = item['name_of_centre']
        type_of_centre = item['type_of_centre']
        location_of_centre = item['location_of_centre']
        zip_code = (location_of_centre.split('S(')[1]).split(')')[0]

        r =requests.get("https://developers.onemap.sg/commonapi/search?searchVal=" + zip_code + "&returnGeom=Y&getAddrDetails=Y&pageNum=1")
        onemap = r.json()

        if(onemap['found'] == 1):
            zipcode_lat = float(onemap['results'][0]['LATITUDE'])
            zipcode_long = float(onemap['results'][0]['LONGITUDE'])
            formattedAddress = onemap['results'][0]['BLK_NO'] + " " + onemap['results'][0]['ROAD_NAME']
            if(Zipcode.objects.filter(zipcode=zip_code).exists()):
                zipcode = Zipcode.objects.get(zipcode= zip_code)
            else:
                zipcode = Zipcode.objects.create(zipcode=zip_code,latitude = zipcode_lat,longitude = zipcode_long,address = formattedAddress.title())

            HawkerCentre.objects.create(centre_name=name_of_centre,
                                        zip_code = zipcode,
                                        centre_type=type_of_centre)
    '''
    #print(request.user.profile.first_name)
    #foodCat = FoodCategory.objects.get(category_name='Korean')

    #for obj in FoodPreferences.objects.filter(food_category_id=3):
    #    print(obj.user_profile.first_name)
    ##for cat in allFoodCats:
    #    print(cat.category_name)
    #Check Exists
    #print(FoodPreferences.objects.filter(user_profile=userProfile,food_category=foodCat).exists())

    #food_preferences = FoodPreferences.objects.create(user_profile=userProfile,food_category=foodCat)
    #print(food_preferences)
    #for row in FoodPreferences.objects.filter(user_profile=userProfile):
    #    print(row.food_category.category_name)

    return render(request, 'homepage.html', {'food_categories':food_categories})


@login_required
def foodstore_page(request,store_id):
    return HttpResponse(store_id)

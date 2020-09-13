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

import os
import sys

@login_required
def homepage(request):
    userProfile = Profile.objects.get(user_id= request.user.id)
    print(userProfile.get_profile_url())
    #print(request.user.profile.first_name)
    foodCat = FoodCategory.objects.get(category_name='Korean')
    allFoodCats = userProfile.food_categories.all()
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

    return render(request, 'homepage.html', {})

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
from Enso.app.controllers.logic.gathering_manager import  upcoming_gatherings,pending_complete_gatherings,get_reviews

import os
import sys
import requests

import cloudinary
import cloudinary.uploader
import cloudinary.api

@login_required
def profilepage(request):
    return render(request, 'profilepage.html',{"upcoming_gatherings":upcoming_gatherings(request.user),
                                              "pending_complete_gatherings": pending_complete_gatherings(request.user),
                                              "reviews":get_reviews(request.user)})

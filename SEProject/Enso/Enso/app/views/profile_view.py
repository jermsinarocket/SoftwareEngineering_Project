from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from Enso.app.models.food_category import FoodCategory
from Enso.app.controllers.logic.gathering_manager import  upcoming_gatherings,pending_complete_gatherings,get_reviews,completed_gatherings

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
                                              "completed_gatherings" : completed_gatherings(request.user),
                                              "reviews":get_reviews(request.user),
                                              "food_categories": FoodCategory.objects.all()})

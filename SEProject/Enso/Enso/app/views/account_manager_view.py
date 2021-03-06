from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.conf import settings
from django.template import loader
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from Enso.app.models.profile import Profile
from Enso.app.models.zipcode import Zipcode
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordResetForm
from django.db.models.query_utils import Q
from django.core.mail import send_mail
from Enso.app.models.food_category import FoodCategory
from Enso.app.models.food_preferences import FoodPreferences
from Enso.app.controllers.logic.cloudinary import uploadFile,deleteFile
from django.views.decorators.csrf import csrf_exempt

import os
import sys

def login(request):
    if request.user.is_authenticated:
        return redirect('homepage')

    food_categories = FoodCategory.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)

        if user is not None:
            auth_login(request, user)
            return redirect('homepage')
        else:
            return render(request,'login.html',{'error':True,'food_categories':food_categories})

    else:
        return render(request, 'login.html', {'food_categories':food_categories})

def register(request):
    if request.method == 'POST':
        post_data = request.POST

        reg_email = post_data['reg_email']
        reg_username = post_data['reg_username']

        error_ids = []

        if(User.objects.filter(username=reg_username).exists()):
            error_ids.append('reg_username_error')

        if(User.objects.filter(email=reg_email).exists()):
            error_ids.append('reg_email_error')

        if(len(error_ids) > 0):
            return JsonResponse({'success':False,'errors':error_ids})
        else:
            try:
                gender = post_data['reg_gender']
                gender = "Male"
            except:
                gender = "Female"

            foodCats = post_data['foodCat'].split(',')

            user = User.objects.create_user(username=reg_username,
                                            email=reg_email,
                                            password=post_data['reg_pwd'])

            userProfile = Profile.objects.get(user_id= user.id)

            profile_pic_id = 'user-default-profile-pic'
            if(len(request.FILES) != 0):
                profile_pic_id = 'profile-pic-user_' + str(userProfile.id)
                uploadFile(request.FILES['file'],profile_pic_id)

            zipcode_lat = float(post_data['zipcode_lat'])
            zipcode_long = float(post_data['zipcode_long'])
            formatted_address = post_data['formatted_address']
            reg_zipcode = post_data['reg_zipcode']

            if(Zipcode.objects.filter(zipcode=reg_zipcode).exists()):
                zipcode = Zipcode.objects.get(zipcode= reg_zipcode)
            else:
                zipcode = Zipcode.objects.create(zipcode=reg_zipcode,latitude = zipcode_lat,longitude = zipcode_long,address = formatted_address.title())

            userProfile.gender = gender
            userProfile.first_name = post_data['reg_firstname']
            userProfile.last_name =  post_data['reg_lastname']
            userProfile.phone_number = post_data['reg_phonenumber']
            userProfile.profile_pic = profile_pic_id
            userProfile.zip_code = zipcode
            userProfile.save()

            for food_cat_id in foodCats:
                FoodPreferences.objects.create(user_profile=userProfile,food_category=FoodCategory.objects.get(pk= food_cat_id))

            return JsonResponse({'success':True})

def resetPassword(request):
    email = request.POST['email'].strip()
    user = User.objects.filter(Q(email=email)).first()
    response = {}
    if user:
        c = {
            'email': user.email,
            'domain': request.META['HTTP_HOST'],
            'site_name': 'Enso',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'user': user,
            'token': default_token_generator.make_token(user),
            'protocol': request.scheme,
        }

        email_template_name='email-templates/password_reset_email.html'
        subject = "Enso - Reset Your Password"
        email = loader.render_to_string(email_template_name, c)
        send_mail(subject, email, '' , [user.email], fail_silently=False)
        response['reset'] = True
    else:
        response['reset'] = False

    return JsonResponse(response)

@login_required
@csrf_exempt
def change_password(request):
    user = User.objects.get(id=request.user.id)
    user.set_password(request.POST['password'])
    user.save()
    return JsonResponse({'success':True})

@login_required
@csrf_exempt
def update_profile(request):
    post_data = request.POST
    user = Profile.objects.get(user_id=request.user.id)
    user.first_name = post_data['first_name']
    user.last_name = post_data['last_name']
    user.save()
    if(len(request.FILES) != 0):
        profile_pic_id = 'profile-pic-user_' + str(request.user.id)
        deleteFile(profile_pic_id)
        uploadFile(request.FILES['file'],profile_pic_id)


    return JsonResponse({'success':True})


@login_required
def logout(request):
    auth_logout(request)
    return redirect('login_user')

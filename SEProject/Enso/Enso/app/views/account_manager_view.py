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
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordResetForm
from django.db.models.query_utils import Q
from django.core.mail import send_mail

import os
import sys

def login(request):
    if request.user.is_authenticated:
        return redirect('homepage')

    password_reset_form = PasswordResetForm()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)

        if user is not None:
            auth_login(request, user)
            return redirect('homepage')
        else:
            login_form = AuthenticationForm()
            return render(request,'login.html',{'login_form':login_form,'pwd_reset_form':password_reset_form,'error':True})

    else:
        login_form = AuthenticationForm()
        password_reset_form = PasswordResetForm()
        #send_mail('Enso - Password Reset', 'Password Reset Request', None, ['weixuan.tan95@gmail.com'])
        return render(request, 'login.html', {'login_form':login_form,'pwd_reset_form':password_reset_form})

def register(request):
    return render()
    
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
def logout(request):
    auth_logout(request)
    return redirect('login_user')

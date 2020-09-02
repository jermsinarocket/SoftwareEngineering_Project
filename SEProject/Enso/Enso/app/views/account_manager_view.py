from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.template import loader
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordResetForm
from django.core.mail import send_mail

import os
import sys


def login(request):
    if request.user.is_authenticated:
        return redirect('/enso')

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

def resetPassword(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        print(password_reset_form)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')

@login_required
def homepage(request):
    return render(request, 'homepage.html', {})

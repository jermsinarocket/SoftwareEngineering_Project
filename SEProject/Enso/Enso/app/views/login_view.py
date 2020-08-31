from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.template import loader
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
import os
import sys


def login(request):
    if request.user.is_authenticated:
        return redirect('/enso')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)

        if user is not None:
            auth_login(request, user)
            return redirect('/enso')
        else:
            login_form = AuthenticationForm()
            return render(request,'login.html',{'login_form':login_form})

    else:
        login_form = AuthenticationForm()
        return render(request, 'login.html', {'login_form':login_form})

def homepage(request):
    return HttpResponse("Logined")

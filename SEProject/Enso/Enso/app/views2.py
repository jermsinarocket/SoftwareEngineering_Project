from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
# Create your views here.

import firebase_admin
import os
import sys
from firebase_admin import credentials
from firebase_admin import firestore
from django.conf import settings

def index(request):

    cred = credentials.Certificate(getattr(settings, "FIREBASE_CRED_PATH_URL",None))
    firebase_admin.initialize_app(cred)

    db = firestore.client()
    users_ref = db.collection(u'users')
    docs = users_ref.stream()
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')
  
    return HttpResponse()
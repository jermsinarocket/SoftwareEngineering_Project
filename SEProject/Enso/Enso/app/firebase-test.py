import firebase_admin
import os
import sys
from firebase_admin import credentials
from firebase_admin import firestore
from django.conf import settings

cred = credentials.Certificate(getattr(settings, "FIREBASE_AUTH"))
firebase_admin.initialize_app(cred)

db = firestore.client()

'''
doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})
'''
users_ref = db.collection(u'users')
docs = users_ref.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')
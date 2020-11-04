"""Enso TOP-LEVEL URL Configuration
"""
from django.contrib import admin
from django.urls import include,path,re_path

BASE_URL_CONTROLLER_DIR = 'Enso.app.controllers.url.'

urlpatterns = [
    path('admin/', admin.site.urls),
    #Account Management URL
    path('', include(BASE_URL_CONTROLLER_DIR + 'account_manager_url')),
    #Main URLS
    path('main/',include(BASE_URL_CONTROLLER_DIR + 'home_manager_url')),
    #Loaders URLS
    path('store/',include(BASE_URL_CONTROLLER_DIR + 'store_manager_url')),
    path('gathering/',include(BASE_URL_CONTROLLER_DIR + 'gathering_manager_url')),
    path('profile/',include(BASE_URL_CONTROLLER_DIR + 'profile_manager_url'))
]

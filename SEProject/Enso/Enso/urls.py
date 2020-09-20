"""Enso TOP-LEVEL URL Configuration
"""
from django.contrib import admin
from django.urls import include,path,re_path

BASE_URL_CONTROLLER_DIR = 'Enso.app.controllers.'

urlpatterns = [
    path('admin/', admin.site.urls),
    #Account Management URL
    path('', include(BASE_URL_CONTROLLER_DIR + 'account_manager_urls_controller')),
    #Main URLS
    path('main/',include(BASE_URL_CONTROLLER_DIR + 'main_urls_controller')),
    #Loaders URLS
    path('loader/',include(BASE_URL_CONTROLLER_DIR + 'loader_urls_controller'))
]

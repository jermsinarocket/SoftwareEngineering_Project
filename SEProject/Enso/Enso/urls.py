"""Enso TOP-LEVEL URL Configuration
"""
from django.contrib import admin
from django.urls import include,path,re_path
from Enso.app.views import account_manager_view

BASE_URL_CONTROLLER_DIR = 'Enso.app.controllers.'
urlpatterns = [
    path('admin/', admin.site.urls),
    #Landing Page redirect
    ##re_path(r'^$', account_manager_view.login, name='login'),
    ##path('logout/',account_manager_view.logout,name='logout'),
    path('', include(BASE_URL_CONTROLLER_DIR + 'account_manager_urls_controller')),
    path('enso/',account_manager_view.homepage,name='homepage')
]

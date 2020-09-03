"""Enso TOP-LEVEL URL Configuration
"""
from django.contrib import admin
from django.urls import include,path,re_path
from Enso.app.views import account_manager_view

BASE_URL_CONTROLLER_DIR = 'Enso.app.controllers.'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(BASE_URL_CONTROLLER_DIR + 'account_manager_urls_controller')),
    path('enso/',include(BASE_URL_CONTROLLER_DIR + 'main_urls_controller')),
    path('accounts/', include('django.contrib.auth.urls'))
]

from django.urls import path,re_path
from Enso.app.views import profile_view

urlpatterns = [
    path('',profile_view.profilepage,name='profile_page')
]

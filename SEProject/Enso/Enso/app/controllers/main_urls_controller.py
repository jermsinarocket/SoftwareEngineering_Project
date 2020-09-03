from django.urls import path
from Enso.app.views import home_view

urlpatterns = [
    path('',home_view.homepage,name='homepage'),
]

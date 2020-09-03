from django.urls import path
from Enso.app.views import home_view

urlpatterns = [
    path('home/',home_view.homepage,name='homepage'),
]

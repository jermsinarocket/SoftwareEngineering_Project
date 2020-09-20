from django.urls import path,re_path
from Enso.app.views import home_view

urlpatterns = [
    path('',home_view.homepage,name='homepage'),
    re_path(r'^store/(?P<store_id>[0-9]+)/$',home_view.foodstore_page,name='storepage')
]

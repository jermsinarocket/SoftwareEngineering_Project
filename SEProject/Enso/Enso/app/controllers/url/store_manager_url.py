from django.urls import path,re_path
from Enso.app.views import store_view

urlpatterns = [
    path('food-listings/',store_view.food_store_listings,name='store_listings'),
    re_path(r'^(?P<store_id>[0-9]+)/$',store_view.food_store,name='storepage')
]

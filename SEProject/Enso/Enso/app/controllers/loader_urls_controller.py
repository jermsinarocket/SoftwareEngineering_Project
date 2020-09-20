from django.urls import path,re_path
from Enso.app.views import loaders

urlpatterns = [
    path('food-listings/',loaders.loadFoodListings,name='load_food_listings')
]

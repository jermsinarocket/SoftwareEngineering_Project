from django.contrib import admin
from django.apps import apps
from app.models.profile import Profile
from app.models.food_category import FoodCategory


class ProfileAdmin(admin.ModelAdmin):
    pass
admin.register(Profile,ProfileAdmin)

class FoodCategoryAdmin(admin.ModelAdmin):
    pass
admin.register(FoodCategory,FoodCategoryAdmin)

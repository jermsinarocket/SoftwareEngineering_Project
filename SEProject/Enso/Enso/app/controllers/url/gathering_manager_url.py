from django.urls import path,re_path
from Enso.app.views import gathering_view

urlpatterns = [
    path('create/new-gathering',gathering_view.create_gathering,name='create_gathering'),
    path('create/new-chat',gathering_view.create_chat,name='create_chat')
]

from django.urls import path,re_path
from Enso.app.views import gathering_view

urlpatterns = [
    path('',gathering_view.gathering_page,name='gathering_page'),
    path('create/new-gathering',gathering_view.create_gathering,name='create_gathering'),
    path('load/existing-gatherings',gathering_view.load_existing_gatherings,name='load_existing_gatherings'),
    path('join/request-join',gathering_view.request_join_gathering,name='request_join_gathering'),
    path('create/new-chat',gathering_view.create_chat,name='create_chat'),
    path('delete/gathering',gathering_view.delete_gathering,name='delete_gathering'),
    path('update/pax',gathering_view.update_pax,name='update_pax')
]

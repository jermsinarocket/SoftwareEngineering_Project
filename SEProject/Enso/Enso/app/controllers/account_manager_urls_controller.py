from django.urls import path
from Enso.app.views import account_manager_view as acct_mng

urlpatterns = [
    path('', acct_mng.login,name= 'login'),
    path('logout/',acct_mng.logout,name='logout')
]

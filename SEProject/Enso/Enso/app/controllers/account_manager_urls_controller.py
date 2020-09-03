from django.urls import path
from Enso.app.views import account_manager_view as acct_mng

urlpatterns = [
    path('', acct_mng.login,name = 'login_user'),
    path('logout/',acct_mng.logout,name='logout_user'),
    path('resetpassword/',acct_mng.resetPassword,name='reset_password')
    path('register/',acct_mng.register,name='register_user')
]

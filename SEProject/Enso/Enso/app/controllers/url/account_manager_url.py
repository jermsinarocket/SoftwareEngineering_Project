from django.urls import path,include
from Enso.app.views import account_manager_view as acct_mng
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', acct_mng.login,name = 'login_user'),
    path('logout/',acct_mng.logout,name='logout_user'),
    path('register/',acct_mng.register,name='register_user'),
    path('change_password',acct_mng.change_password,name='change_password'),
    path('resetpassword/',acct_mng.resetPassword,name='reset_password'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete')
]

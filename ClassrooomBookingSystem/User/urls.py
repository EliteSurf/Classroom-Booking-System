from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # import local app view

urlpatterns = [
    path('SignUp/', views.sign_up, name='Sign-Up'),
    path('SignIn/', auth_views.LoginView.as_view(template_name='User/SignIn.html'), name='Sign-In'),
    path('SignOut/', auth_views.LogoutView.as_view(template_name='User/SignOut.html'), name='Sign-Out'),
    path('Reset_Password/', auth_views.PasswordResetView.as_view(
        template_name='User/Reset_Password.html'), name='Reset-Password'),
    path('Reset_Password/Done/', auth_views.PasswordResetDoneView.as_view(
        template_name='User/Reset_Password_Done.html'), name='password_reset_done'),
    path('Reset_Password/Confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='User/Reset_Password_Confirm.html'), name='password_reset_confirm'),
    path('Reset_Password/Complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='User/Reset_Password_Complete.html'), name='password_reset_complete'),
    path('Profile/', views.profile, name='Profile'),
    path('Profile/<int:id>', views.profile_update, name='Profile-Update'),
    path('Change_Password', views.change_password, name='Change-Password'),
]

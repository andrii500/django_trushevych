from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    url('registration/', views.RegistrationView.as_view(), name='registration'),
    path('login/', views.LogInView.as_view(), name='login'),
    path('logout/', views.LogOutView.as_view(), name='logout'),

    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='password/password_reset.html'),
        name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password/password_reset_done.html'),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password/password_reset_complete.html'),
        name='password_reset_complete'),

    path('password_change/', views.MyPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='password/password_change_done.html'),
        name='password_change_done'),
]

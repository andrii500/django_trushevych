from django.conf.urls import url
from django.urls import path, include
from . import views


urlpatterns = [
    url('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login_custom'),
]

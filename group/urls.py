from django.urls import path

from . import views


urlpatterns = [
    path('groups/', views.get_groups, name='groups'),
    path('create-group/', views.create_group_from_model, name='create-group'),
]

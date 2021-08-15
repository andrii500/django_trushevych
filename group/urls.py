from django.urls import path
from . import views


urlpatterns = [
    path('groups/', views.get_groups, name='groups'),
    path('create-group/', views.create_group_from_model, name='create-group'),
    path('edit-group/<int:group_id>', views.edit_group, name='edit-group'),
    path('delete-group/<int:group_id>', views.delete_group, name='delete-group')
]

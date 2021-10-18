from django.urls import path
from . import views


urlpatterns = [
    path('groups/', views.GroupListView.as_view(), name='groups'),
    path('create-group/', views.CreateGroupFormView.as_view(), name='create-group'),
    path('edit-group/<int:pk>/', views.EditGroupView.as_view(), name='edit-group'),
    path('delete-group/<int:pk>/', views.DeleteGroupView.as_view(), name='delete-group')
]

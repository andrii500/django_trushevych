from django.urls import path
from . import views


urlpatterns = [
    path('teachers/', views.TeacherListView.as_view(), name='teachers'),
    path('create-teacher/', views.CreateTeacherFormView.as_view(), name='create-teacher'),
    path('edit-teacher/<int:pk>/', views.EditTeacherView.as_view(), name='edit-teacher'),
    path('delete-teacher/<int:pk>/', views.DeleteTeacherView.as_view(), name='delete-teacher')
]

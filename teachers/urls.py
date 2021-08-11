from django.urls import path
from . import views


urlpatterns = [
    path('teachers/', views.get_teachers, name='teachers'),
    path('create-teacher/', views.create_teacher_from_model, name='create-teacher'),
    path('edit-teacher/<int:teacher_id>', views.edit_teacher, name='edit-teacher'),
    path('delete-teacher/<int:teacher_id>', views.delete_teacher, name='delete-teacher')
]

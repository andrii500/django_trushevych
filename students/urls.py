from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.get_students, name='students'),
    path('generate-student/', views.get_generate_student, name='generate-student'),
    path('generate-students/', views.get_generate_students, name='generate-students'),
    path('create-student/', views.create_student_from_model, name='create-student'),

    path('edit-student/<int:student_id>', views.edit_student, name='edit-student'),
    path('delete-student/<int:student_id>', views.delete_student, name='delete-student'),
    path('generate-students-form/', views.manually_generate_students, name='generate-students-form'),

    path('email-sending-form/', views.sending_email, name='email-sending-form'),
]

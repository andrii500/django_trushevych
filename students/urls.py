from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.get_students, name='get-students'),
    path('generate-student/', views.get_generate_student, name='generate-student'),
    path('generate-students/', views.get_generate_students, name='generate-students'),
    path('create-student/', views.create_student_from_model, name='create-student'),
]

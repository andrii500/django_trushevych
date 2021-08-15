from django.urls import path

from . import views


urlpatterns = [
    path('teachers/', views.get_teachers, name='teachers'),
    path('create-teacher/', views.create_teacher_from_model, name='create-teacher'),
]

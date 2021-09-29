from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('students/', views.StudentListView.as_view(), name='students'),
    path('generate-student/', views.GenerateStudentView.as_view(), name='generate-student'),
    path('generate-students/', views.GenerateStudentsView.as_view(), name='generate-students'),
    path('create-student/', views.CreateStudentFormView.as_view(), name='create-student'),
    path('edit-student/<int:pk>/', views.EditStudentView.as_view(), name='edit-student'),
    path('delete-student/<int:pk>/', views.DeleteStudentView.as_view(), name='delete-student'),
    path('generate-students-form/', views.ManuallyGenerateStudentsFormView.as_view(), name='generate-students-form'),
    path('email-sending-form/', views.SendingEmailView.as_view(), name='email-sending-form'),
]

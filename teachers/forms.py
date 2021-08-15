from django import forms

from .models import Teacher


class TeacherFormFromModel(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'subject', 'age']

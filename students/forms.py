from django import forms

from .models import Student


class StudentFormFromModel(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age']

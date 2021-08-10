from django import forms

from .models import Group


class GroupFormFromModel(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['title', 'num_of_students']

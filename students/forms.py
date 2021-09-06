import re

from django import forms
from django.core.exceptions import ValidationError


def phone_number_validation(phone_number):
    if not re.match(r"^\+380\d{9}$", phone_number):
        raise ValidationError(f"{phone_number}: Phone number format - +380xxxxxxxxx")


class StudentForm(forms.Form):
    first_name = forms.CharField(label="First name", required=True, max_length=100)
    last_name = forms.CharField(label="Last name", required=True, max_length=100)
    age = forms.IntegerField(label="Age", required=True)
    phone = forms.CharField(label="Phone", required=True,
                            empty_value=None, validators=[phone_number_validation],
                            widget=forms.TextInput(attrs={'placeholder': '+380xxxxxxxxx'}))

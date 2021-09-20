import re

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


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


class GenerateRandomStudentForm(forms.Form):
    total = forms.IntegerField(
        validators=[
            MinValueValidator(10),
            MaxValueValidator(500)
        ]
    )


class ContactUsForm(forms.Form):
    title = forms.CharField(label='Title', required=True, max_length=200)
    message = forms.CharField(label='Text message', required=True, max_length=2000,
                              widget=forms.Textarea(attrs={'placeholder': 'Enter message', 'rows': 10, 'cols': 50}))
    email_from = forms.EmailField(label='email', required=True, max_length=100,
                                  widget=forms.EmailInput(attrs={'placeholder': 'example@mail.com'}))

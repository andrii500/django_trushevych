from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LogInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class MyPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User

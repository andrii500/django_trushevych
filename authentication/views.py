from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import RegistrationForm, LogInForm, MyPasswordChangeForm


class RegistrationView(SuccessMessageMixin, CreateView):
    form_class = RegistrationForm
    template_name = 'authentication/registration.html'
    success_message = 'User was create successfully'
    success_url = reverse_lazy('index')


class LogInView(SuccessMessageMixin, LoginView):
    form_class = LogInForm
    template_name = 'authentication/login.html'
    success_message = 'Successfully logged in.'


class LogOutView(LogoutView):
    next_page = 'index'


class MyPasswordChangeView(PasswordChangeView):
    form_class = MyPasswordChangeForm
    template_name = 'password/password_change.html'

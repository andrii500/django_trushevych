from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView, View, FormView, UpdateView, DeleteView
from django.contrib import messages
from faker import Faker
from .models import Student
from .forms import StudentForm, GenerateRandomStudentForm, ContactUsForm
from .tasks import create_random_students, send_email

from django.contrib.auth.decorators import login_required

faker = Faker()


def fake_phone_number(fake):
    return f'+380{fake.msisdn()[4:]}'


# @login_required(login_url='login/')
class IndexView(TemplateView):
    template_name = 'base/index.html'


class StudentListView(ListView):
    model = Student

    def get_queryset(self):
        args = self.request.GET
        dict_param = {}
        for key, value in args.items():
            dict_param[key] = value

        queryset = Student.objects.filter(**dict_param)
        return queryset


class GenerateStudentView(View):

    def get(self, request, *args, **kwargs):
        Student.objects.create(first_name=faker.first_name(),
                               last_name=faker.last_name(),
                               age=faker.random_int(18, 100),
                               phone=fake_phone_number(faker))
        return redirect('students')


class GenerateStudentsView(View):

    def get(self, request, *args, **kwargs):
        count = request.GET.get("count", "1")
        if count.isdigit():
            if 0 < int(count) <= 100:
                for i in range(int(count)):
                    Student.objects.create(first_name=faker.first_name(),
                                           last_name=faker.last_name(),
                                           age=faker.random_int(18, 100),
                                           phone=fake_phone_number(faker))
                return redirect('students')
            else:
                return HttpResponse("Count must be greater than 0, less or equal  than 100")
        else:
            return HttpResponse("Count must be integer and not negative")


class CreateStudentFormView(FormView):
    template_name = 'students/student_from_model.html'
    form_class = StudentForm

    def form_valid(self, form):
        Student.objects.create(**form.cleaned_data)
        return redirect('students')


class EditStudentView(UpdateView):
    model = Student
    template_name = 'students/student_edit_form.html'
    form_class = StudentForm
    success_url = reverse_lazy('students')


class DeleteStudentView(DeleteView):
    model = Student
    success_url = reverse_lazy('students')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


class ManuallyGenerateStudentsFormView(FormView):
    template_name = 'students/student_generator.html'
    form_class = GenerateRandomStudentForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_students.delay(total)
        messages.success(self.request, 'We are generate a random students! Wait a moment and refresh this page.')
        return redirect('students')


class SendingEmailView(FormView):
    template_name = 'email/email_sending_form.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('email-sending-form')

    def form_valid(self, form):
        title = form.cleaned_data.get('title')
        message = form.cleaned_data.get('message')
        email_from = form.cleaned_data.get('email_from')
        send_email.delay(title, message, email_from)
        messages.success(self.request, 'E-mail was sent!')
        return super().form_valid(form)


def handler404(request, exception):
    return render(request, 'errors/404_error.html', status=404)


def handler500(request):
    return render(request, 'errors/500_error.html', status=500)

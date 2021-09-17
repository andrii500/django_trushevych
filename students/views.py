from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from faker import Faker
from .models import Student
from .forms import StudentForm

faker = Faker()


def index(request):
    return HttpResponse("""<h2>Students</h2>
                           <p>Path: /students/</p>
                           <p>Path: /students/?first_name=value&last_name=value&age=value</p>
                           <p>Path: /generate-student/</p>
                           <p>Path: /generate-students/?count=value</p>
                           <p>Path: /create-student/</p>
                           <p>Path: /edit-student/student_id</p>
                           <p>Path: /delete-student/student_id</p>
                           <h2>Teachers</h2>
                           <p>Path: /teachers/</p>
                           <p>Path: /teachers/?first_name=value&last_name=value&age=value</p>
                           <p>Path: /create-teacher/</p>
                           <p>Path: /edit-teacher/teacher_id</p>
                           <p>Path: /delete-teacher/teacher_id</p>
                           <h2>Groups</h2>
                           <p>Path: /groups/</p>
                           <p>Path: /create-group/</p>
                           <p>Path: /edit-group/group_id</p>
                           <p>Path: /delete-group/group_id</p>""")


def get_students(request):
    args = request.GET
    dict_param = {}
    for key, value in args.items():
        dict_param[key] = value
    if dict_param:
        students_list = Student.objects.filter(**dict_param)
        return render(request, 'students.html', {'students': students_list})
    else:
        students_list = Student.objects.all()
        return render(request, 'students.html', {'students': students_list})


def fake_phone_number(fake):
    return f'+380{fake.msisdn()[4:]}'


def get_generate_student(request):
    Student.objects.create(first_name=faker.first_name(), last_name=faker.last_name(), age=faker.random_int(18, 100),
                           phone=fake_phone_number(faker))
    return HttpResponseRedirect(reverse('students'))


def get_generate_students(request):
    count = request.GET.get("count", "1")
    if count.isdigit():
        if 0 < int(count) <= 100:
            for i in range(int(count)):
                Student.objects.create(first_name=faker.first_name(),
                                       last_name=faker.last_name(),
                                       age=faker.random_int(18, 100),
                                       phone=fake_phone_number(faker))
            return HttpResponseRedirect(reverse('students'))
        else:
            return HttpResponse("Count must be greater than 0, less or equal  than 100")
    else:
        return HttpResponse("Count must be integer and not negative")


def create_student_from_model(request):
    if request.method == 'GET':
        form = StudentForm()
    elif request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            Student.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(reverse('students'))

    return render(request, 'student_from_model.html', {'form': form})


def edit_student(request, student_id):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            Student.objects.update_or_create(defaults=form.cleaned_data, id=student_id)
            return HttpResponseRedirect(reverse('students'))
    else:
        student = Student.objects.filter(id=student_id).first()
        form = StudentForm(instance=student)

    return render(request, 'student_edit_form.html', {'form': form, 'student_id': student_id})


def delete_student(request, student_id):
    student = Student.objects.filter(id=student_id)
    student.delete()
    return HttpResponseRedirect(reverse('students'))

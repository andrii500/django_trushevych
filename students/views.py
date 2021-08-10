from django.http import HttpResponse

from django.shortcuts import render

from faker import Faker

from .models import Student

from .forms import StudentFormFromModel


faker = Faker()


def index(request):
    return HttpResponse("""<h2>Students</h2>
                           <p>Path: /students/</p>
                           <p>Path: /generate-student/</p>
                           <p>Path: /generate-students/?count=value</p>
                           <p>Path: /create-student/</p>
                           <h2>Teachers</h2>
                           <p>Path: /teachers/</p>
                           <p>Path: /create-teacher/</p>
                           <p>Path: /teachers/?first_name=value&last_name=value&age=value</p>
                           <h2>Groups</h2>
                           <p>Path: /groups/</p>
                           <p>Path: /create-group/</p>""")


def get_students(request):
    args = request.GET
    dict_param = {}
    for key, value in args.items():
        dict_param[key] = value
    if dict_param:
        students_list = Student.objects.filter(**dict_param)
        output = ''.join([f"<p>{s.id}. {s.first_name} {s.last_name}, {s.age}</p>" for s in students_list])
        return HttpResponse(f"{output}")
    else:
        students_list = Student.objects.all()
        output = ''.join([f"<p>{s.id}. {s.first_name} {s.last_name}, {s.age}</p>" for s in students_list])
        return HttpResponse(f"{output}")


def get_generate_student(request):
    student = Student.objects.create(first_name=faker.first_name(),
                                     last_name=faker.last_name(),
                                     age=faker.random_int(18, 100))
    return HttpResponse(f"{student.id}, "
                        f"{student.first_name}, "
                        f"{student.last_name}, "
                        f"{student.age}")


def get_generate_students(request):
    count = request.GET.get("count", "1")
    if count.isdigit():
        if 0 < int(count) <= 100:
            output = ''
            for i in range(int(count)):
                student = Student.objects.create(first_name=faker.first_name(),
                                                 last_name=faker.last_name(),
                                                 age=faker.random_int(18, 100))
                output += f"<p>{student.id}, {student.first_name}, {student.last_name}, {student.age}</p>"
            return HttpResponse(output)
        else:
            return HttpResponse("Count must be greater than 0, less or equal  than 100")
    else:
        return HttpResponse("Count must be integer and not negative")


def create_student_from_model(request):
    if request.method == 'GET':
        form = StudentFormFromModel()
    elif request.method == 'POST':
        form = StudentFormFromModel(request.POST)

        if form.is_valid():
            Student.objects.create(**form.cleaned_data)
            return HttpResponse('Student created!')

    return render(request, 'student_from_model.html', {'form': form})

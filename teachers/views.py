from django.http import HttpResponse

from django.shortcuts import render

from faker import Faker

from .models import Teacher

from .forms import TeacherFormFromModel

faker = Faker()


def get_teachers(request):
    args = request.GET
    dict_param = {}
    for key, value in args.items():
        dict_param[key] = value
    if dict_param:
        teachers_list = Teacher.objects.filter(**dict_param)
        output = ''.join([f"<p>{t.id}. {t.first_name} {t.last_name}, {t.age}, {t.subject}</p>" for t in teachers_list])
        return HttpResponse(f"{output}")
    else:
        teachers_list = Teacher.objects.all()
        output = ''.join([f"<p>{t.id}. {t.first_name} {t.last_name}, {t.age}, {t.subject}</p>" for t in teachers_list])
        return HttpResponse(f"{output}")


def create_teacher_from_model(request):
    if request.method == 'GET':
        form = TeacherFormFromModel()
    elif request.method == 'POST':
        form = TeacherFormFromModel(request.POST)

        if form.is_valid():
            Teacher.objects.create(**form.cleaned_data)
            return HttpResponse('Teacher created!')

    return render(request, 'teacher_from_model.html', {'form': form})

from django.http import HttpResponseRedirect
from django.urls import reverse
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
        return render(request, 'teachers.html', {'teachers': teachers_list})
    else:
        teachers_list = Teacher.objects.all()
        return render(request, 'teachers.html', {'teachers': teachers_list})


def create_teacher_from_model(request):
    if request.method == 'GET':
        form = TeacherFormFromModel()
    elif request.method == 'POST':
        form = TeacherFormFromModel(request.POST)

        if form.is_valid():
            Teacher.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(reverse('teachers'))

    return render(request, 'teacher_from_model.html', {'form': form})


def edit_teacher(request, teacher_id):
    if request.method == 'POST':
        form = TeacherFormFromModel(request.POST)
        if form.is_valid():
            Teacher.objects.update_or_create(defaults=form.cleaned_data, id=teacher_id)
            return HttpResponseRedirect(reverse('teachers'))
    else:
        teacher = Teacher.objects.filter(id=teacher_id).first()
        form = TeacherFormFromModel(instance=teacher)

    return render(request, 'teacher_edit_form.html', {'form': form, 'teacher_id': teacher_id})


def delete_teacher(request, teacher_id):
    teacher = Teacher.objects.filter(id=teacher_id)
    teacher.delete()
    return HttpResponseRedirect(reverse('teachers'))

from django.http import HttpResponse

from django.shortcuts import render

from faker import Faker

from .models import Group

from .forms import GroupFormFromModel

faker = Faker()


def get_groups(request):
    group_list = Group.objects.all()
    output = ''.join(
        [f"<p>{t.title}, {t.num_of_students}</p>" for t in group_list]
    )
    return HttpResponse(f"{output}")


def create_group_from_model(request):
    if request.method == 'GET':
        form = GroupFormFromModel()
    elif request.method == 'POST':
        form = GroupFormFromModel(request.POST)

        if form.is_valid():
            Group.objects.create(**form.cleaned_data)
            return HttpResponse('Group created!')

    return render(request, 'group_from_model.html', {'form': form})

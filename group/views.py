from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from faker import Faker
from .models import Group
from .forms import GroupFormFromModel

faker = Faker()


def get_groups(request):
    groups_list = Group.objects.all()
    return render(request, 'groups.html', {'groups': groups_list})


def create_group_from_model(request):
    if request.method == 'GET':
        form = GroupFormFromModel()
    elif request.method == 'POST':
        form = GroupFormFromModel(request.POST)

        if form.is_valid():
            Group.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(reverse('groups'))

    return render(request, 'group_from_model.html', {'form': form})


def edit_group(request, group_id):
    if request.method == 'POST':
        form = GroupFormFromModel(request.POST)
        if form.is_valid():
            Group.objects.update_or_create(defaults=form.cleaned_data, id=group_id)
            return HttpResponseRedirect(reverse('groups'))
    else:
        group = Group.objects.filter(id=group_id).first()
        form = GroupFormFromModel(instance=group)

    return render(request, 'group_edit_form.html', {'form': form, 'group_id': group_id})


def delete_group(request, group_id):
    group = Group.objects.filter(id=group_id)
    group.delete()
    return HttpResponseRedirect(reverse('groups'))

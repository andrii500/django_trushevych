from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView, FormView, UpdateView, DeleteView
from .models import Group
from .forms import GroupFormFromModel


class GroupListView(ListView):
    model = Group


class CreateGroupFormView(FormView):
    template_name = 'group/group_from_model.html'
    form_class = GroupFormFromModel

    def form_valid(self, form):
        Group.objects.create(**form.cleaned_data)
        return redirect('groups')


class EditGroupView(UpdateView):
    model = Group
    template_name = 'group/group_edit_form.html'
    form_class = GroupFormFromModel
    success_url = reverse_lazy('groups')


class DeleteGroupView(DeleteView):
    model = Group
    success_url = reverse_lazy('groups')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

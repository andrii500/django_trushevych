from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView, FormView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Group
from .forms import GroupFormFromModel


class GroupListView(ListView):
    model = Group


class CreateGroupFormView(LoginRequiredMixin, FormView):
    form_class = GroupFormFromModel
    template_name = 'group/group_from_model.html'
    login_url = '/login/'

    def form_valid(self, form):
        Group.objects.create(**form.cleaned_data)
        return redirect('groups')


class EditGroupView(LoginRequiredMixin, UpdateView):
    model = Group
    form_class = GroupFormFromModel
    template_name = 'group/group_edit_form.html'
    success_url = reverse_lazy('groups')
    login_url = '/login/'


class DeleteGroupView(LoginRequiredMixin, DeleteView):
    model = Group
    success_url = reverse_lazy('groups')
    login_url = '/login/'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

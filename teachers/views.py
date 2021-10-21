from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView, FormView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Teacher
from .forms import TeacherFormFromModel


class TeacherListView(ListView):
    model = Teacher

    def get_queryset(self):
        args = self.request.GET
        dict_param = {}
        for key, value in args.items():
            dict_param[key] = value

        queryset = Teacher.objects.filter(**dict_param)
        return queryset


class CreateTeacherFormView(LoginRequiredMixin, FormView):
    form_class = TeacherFormFromModel
    template_name = 'teachers/teacher_from_model.html'
    login_url = '/login/'

    def form_valid(self, form):
        Teacher.objects.create(**form.cleaned_data)
        return redirect('teachers')


class EditTeacherView(LoginRequiredMixin, UpdateView):
    model = Teacher
    form_class = TeacherFormFromModel
    template_name = 'teachers/teacher_edit_form.html'
    success_url = reverse_lazy('teachers')
    login_url = '/login/'


class DeleteTeacherView(LoginRequiredMixin, DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers')
    login_url = '/login/'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

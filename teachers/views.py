from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView, FormView, UpdateView, DeleteView
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


class CreateTeacherFormView(FormView):
    template_name = 'teachers/teacher_from_model.html'
    form_class = TeacherFormFromModel

    def form_valid(self, form):
        Teacher.objects.create(**form.cleaned_data)
        return redirect('teachers')


class EditTeacherView(UpdateView):
    model = Teacher
    template_name = 'teachers/teacher_edit_form.html'
    form_class = TeacherFormFromModel
    success_url = reverse_lazy('teachers')


class DeleteTeacherView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

from django.contrib import admin
from .models import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'num_of_students', 'main_student', 'main_teacher')
    list_filter = ('title',)
    search_fields = ('title__startswith',)

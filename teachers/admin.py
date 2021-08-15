from django.contrib import admin
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'age', 'subject')
    list_filter = ('last_name', 'first_name', 'subject')
    search_fields = ('last_name__startswith',)

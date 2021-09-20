from django.contrib import admin
from .models import Student, Logger


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'age', 'phone')
    list_filter = ('last_name', 'first_name')
    search_fields = ('last_name__startswith',)


@admin.register(Logger)
class LoggerAdmin(admin.ModelAdmin):
    list_display = ('id', 'method', 'path', 'execution_time', 'created')

from django.contrib import admin
from .models import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'num_of_students')
    list_filter = ('title',)
    search_fields = ('title__startswith',)

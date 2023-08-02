from django.contrib import admin
from .models import TodoModel


@admin.register(TodoModel)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'due_date', 'status']

from rest_framework import serializers
from .models import TodoModel


class ToDoSeriliazer(serializers.ModelSerializer):

    class Meta:
        model = TodoModel
        fields = ['id', 'title', 'description', 'due_date', 'status']
        
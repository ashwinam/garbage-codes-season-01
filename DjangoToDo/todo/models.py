from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ToDoTbl(models.Model):
    STATUS = [
        ('In Progress', 'In Progress'),
        ('Complete', 'Complete')
    ]
    todo_id = models.AutoField(primary_key=True)
    todo_name = models.CharField(max_length=100)
    todo_description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='In Progress')
    add_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.todo_name)
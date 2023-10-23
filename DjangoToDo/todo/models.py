from django.db import models

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
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.todo_name)
from django.db import models

class TodoModel(models.Model):

    STATUS = [
        ('Completed', 'Completed'),
        ('In Progress', 'In Progress'),
        ('Not Completed', 'Not Completed')
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=50, choices=STATUS)

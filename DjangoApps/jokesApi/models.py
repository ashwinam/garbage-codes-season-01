from django.db import models


class JokesModel(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    categories = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.title)

from rest_framework import serializers
from .models import JokesModel


class JokesSerializer(serializers.ModelSerializer):

    class Meta:
        model = JokesModel
        fields = ['id', 'title', 'text', 'categories']

from typing import Any
from django.core.exceptions import ValidationError
from django import forms
from .models import ToDoTbl

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoTbl
        fields = ['todo_name', 'todo_description']

        widgets = {
            'todo_name': forms.TextInput
            (attrs={
                'class': 'form-control', 
                'placeholder':"ToDo ...", 
                'id': "todo_name_id",
                'name': 'todo_name'
                }),
            'todo_description': forms.Textarea(attrs={
                'class':"form-control",
                'id':"todo_description_id",
                'rows':"3",
                'name':"todo_description",
                'placeholder':"Description ..."
            })
        }
    
    
    def clean_todo_name(self):
        data = self.cleaned_data.get('todo_name', None)
        if data:
            if ToDoTbl.objects.filter(todo_name=data).exists():
                raise ValidationError('%(value)s -- todo is already exists, please change the name', params={'value': data})
        return data
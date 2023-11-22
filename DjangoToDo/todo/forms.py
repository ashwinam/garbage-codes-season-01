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
                'placeholder':"Name ...", 
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
    
    def __init__(self,*args,**kwargs):
        data = kwargs.get('data')
        self.todo_id = ''
        if data:   
            self.todo_id = data.get('todo_id', None)
            self.user = data.get('user', None)
        super(ToDoForm,self).__init__(*args,**kwargs)
    
    def clean_todo_name(self):
        data = self.cleaned_data.get('todo_name', None)
        if self.todo_id:
            if ToDoTbl.objects.filter(todo_name=data, add_by=self.user).exclude(todo_id=self.todo_id).exists():
                raise ValidationError('%(value)s is already exists, please change the name', params={'value': data})
        else:
            if ToDoTbl.objects.filter(todo_name=data, add_by=self.user).exists():
                raise ValidationError('%(value)s is already exists, please change the name', params={'value': data})
        return data
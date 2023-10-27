from django import forms
from .models import ToDoTbl

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoTbl
        fields = ['todo_name', 'todo_description']
    
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.fields['todo_name'].widget.attrs.update(
            {'class': 'form-control', 
             'placeholder':"ToDo ...", 
             'id': "todo_name_id",
             'name': 'todo_name'
             }
            )

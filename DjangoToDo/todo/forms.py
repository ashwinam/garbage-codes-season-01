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
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(self, *args, **kwargs)
    #     self.fields['todo_name'].widget.attrs.update(
    #         {'class': 'form-control', 
    #          'placeholder':"ToDo ...", 
    #          'id': "todo_name_id",
    #          'name': 'todo_name'
    #          }
    #         )

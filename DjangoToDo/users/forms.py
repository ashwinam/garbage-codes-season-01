from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)
        print(fields, '--')


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
    
        widgets = {
            'username': forms.TextInput
            (attrs={
                'type': 'text',
                'class': 'form-control', 
                'placeholder':"Please, enter a username.", 
                'id': "id_username",
                'name': 'username'
                }),
            'password': forms.PasswordInput
            (attrs={
                'type': 'password',
                'class': 'form-control', 
                'placeholder':"Please, enter a password.", 
                'id': "password",
                'name': 'id_password'
                })}
        
    def __init__(self, *args, **kwargs):
        # self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
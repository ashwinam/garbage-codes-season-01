from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email","password1", 'password2')
        UserCreationForm.base_fields['password1'].widget.attrs['class'] = 'form-control'
        UserCreationForm.base_fields['password1'].widget.attrs['placeholder'] = 'Enter the password'
        UserCreationForm.base_fields['password2'].widget.attrs['class'] = 'form-control'
        UserCreationForm.base_fields['password2'].widget.attrs['placeholder'] = 'Re-enter your password'
        

        widgets = {
            'username': forms.TextInput
            (attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder':"Please, enter a username.",
        }),
            'email': forms.EmailInput
            (attrs={
                'type': 'email',
                'class': 'form-control',
                'placeholder':"Please, enter a Email Address.",
        }),
            'password1': forms.PasswordInput
            (attrs={
                'type': 'password',
                'name': 'password1',
                'class': 'form-control',
                'placeholder':"Please, enter a password.",
        }),
            'password2': forms.PasswordInput
            (attrs={
                'type': 'password',
                'name': 'password2',
                'class': 'form-control',
                'placeholder':"Please, enter a password again.",
        }),
        }


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
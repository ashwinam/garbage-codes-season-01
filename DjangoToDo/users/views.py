from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import LoginForm
# Create your views here.


class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = LoginForm
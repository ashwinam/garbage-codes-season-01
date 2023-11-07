from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from .forms import LoginForm
# Create your views here.


class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

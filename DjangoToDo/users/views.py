from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm

class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True


class UserRegistration(CreateView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    model = User
    success_url = reverse_lazy('todos')
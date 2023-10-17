from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import CustomUserCreationForm

# Create your views here.
def dashboard(request):
    return render(request, 'users/dashboard.html')

def register(request):
    if request.method == "GET":
        return render(
            request, "registration/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))
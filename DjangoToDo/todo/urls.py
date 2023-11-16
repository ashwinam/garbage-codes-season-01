from django.urls import path
from django.contrib.auth.forms import UserCreationForm
from . import views

# URLS

urlpatterns = [
    path('', views.index.as_view(), name='home'),
    path('todo/', views.ToDoView.as_view(), name='todos'),
]

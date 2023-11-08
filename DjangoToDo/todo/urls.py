from django.urls import path
from . import views

# URLS

urlpatterns = [
    path('', views.index, name='home'),
    path('todo/', views.ToDoView.as_view(), name='todos'),
]

from django.urls import path
from . import views

# URLS

urlpatterns = [
    path('', views.index),
    path('todo/', views.ToDoView.as_view(), name='todos'),
    path('todo/<int:pk>/', views.ToDoUpdateView.as_view(), name='todo'),
]

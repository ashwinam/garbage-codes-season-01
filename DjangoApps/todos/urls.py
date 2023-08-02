from django.urls import path
from . import views

urlpatterns = [
    path('', views.ToDOClassView.as_view()),
    path('<int:pk>/', views.ToDoDetailView.as_view()),
    path('todos/', views.ToDoView.as_view()),
    path('todos/<int:pk>/', views.ToDoDetail.as_view()),

]

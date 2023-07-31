from django.urls import path
from . import views

urlpatterns = [
    # path('', views.ToDoView.as_view()),
    path('', views.ToDOClassView.as_view()),
    path('<int:pk>/', views.ToDoDetailView.as_view()),


]



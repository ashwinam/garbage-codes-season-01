from django.urls import path
from . import views

urlpatterns = [
    path('', views.JokesView.as_view())
]

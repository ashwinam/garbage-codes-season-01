from django.urls import path, include
from . import views

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("login/", views.UserLoginView.as_view(), name='login'),
]

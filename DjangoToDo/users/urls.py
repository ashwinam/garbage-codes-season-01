from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    # path("", include("django.contrib.auth.urls")),
    path("login/", views.UserLoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
]

from django.urls import path
from user.views import dashboard

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
]
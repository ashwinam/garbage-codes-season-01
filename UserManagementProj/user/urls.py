from django.urls import path, include
from user.views import dashboard, register


'''
    path('accounts/', include("django.contrib.auth.urls")),
    this will give you access to all of the following URLs:
    1. accounts/login
    2. accounts/logout
    3. accounts/password_change
    4. accounts/password_change/done
    5. accounts/password_reset/
    6. accounts/password_reset/done
    7. accounts/reset/<uidb64>/<token>/
    8. accounts/reset/done/
    '''
urlpatterns = [
    path('accounts/', include("django.contrib.auth.urls")),
    path("dashboard/", dashboard, name="dashboard"),
    path("oauth/", include("social_django.urls")),
    path("register/", register, name="register"),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todos.urls')),
    path('weather/', include('weatherReport.urls')),
    path('jokes/', include('jokesApi.urls')),
]

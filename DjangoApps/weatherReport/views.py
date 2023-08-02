from django.shortcuts import HttpResponse


def Index(request):
    return HttpResponse('Welcome to the weather report.')

# Tomorrow register a weatherapi.com get a key and read about  django.core.wsgi requests module

# create a url str:city_name, or find how to pass the data from frontend side

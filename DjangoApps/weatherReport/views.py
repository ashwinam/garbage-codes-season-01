from django.shortcuts import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests


@api_view()
def city_wise_weather(request, city_name):
    base_url = 'http://api.weatherapi.com/v1/current.json'

    params = {
        "key": '5cc53c5ddc5d4dc7860160219230308',
        "q": city_name
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:

        return Response(response.json())

    return Response({'message': 'Welcome to the weather report.'})

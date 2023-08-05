from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import JokesModel
from .serializers import JokesSerializer

import random
import traceback


class JokesView(APIView):

    def get(self, request):
        try:
            category = request.GET.get('category', None)
            queryset = JokesModel.objects.all()
            if category:
                queryset = JokesModel.objects.filter(
                    categories__iexact=category)
                if not queryset:
                    return Response({'error': "Not containing any associated jokes with this category."}, status=status.HTTP_404_NOT_FOUND)

            # getting random quote from collection
            joke_obj = random.choice(list(queryset))
            serializer = JokesSerializer(joke_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': "Something went wrong."}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = JokesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

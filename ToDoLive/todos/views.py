from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from .serializers import ToDoSeriliazer
from .models import TodoModel


class ToDoView(APIView):

    def get(self, request):
        queryset = TodoModel.objects.all()
        serializer = ToDoSeriliazer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ToDoSeriliazer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ToDoDetail(APIView):

    def get(self, request, pk):
        instance = get_object_or_404(TodoModel, pk=pk)
        serializer = ToDoSeriliazer(instance=instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        instance = get_object_or_404(TodoModel, pk=pk)
        serializer = ToDoSeriliazer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        instance = get_object_or_404(TodoModel, pk=pk)
        instance.delete()
        return Response('{message: Object deleted successfully.}', status=status.HTTP_204_NO_CONTENT)


class ToDOClassView(ListCreateAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = ToDoSeriliazer


class ToDoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = ToDoSeriliazer

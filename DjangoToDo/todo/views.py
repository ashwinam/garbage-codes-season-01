from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView, ListView
from .models import ToDoTbl

# Create your views here.

def index(request):
    return render(request, 'base.html')

class ToDoView(ListView):
    model = ToDoTbl
    template_name = 'todo/todo.html'
    context_object_name = "objects"

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

    def post(self, *args, **kwargs):
        todo_name = self.request.POST.get('todo_name', None)
        todo_desc = self.request.POST.get('todo_description', None)
        
        # Object creation.
        obj = ToDoTbl(todo_name=todo_name, todo_description=todo_desc)
        obj.save()

        queryset = self.model.objects.all()

        return render(self.request, 'todo/todo.html', {'objects': queryset})
from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView, ListView
from .models import ToDoTbl
from .forms import ToDoForm

# Create your views here.

def index(request):
    return render(request, 'base.html')

class ToDoView(ListView):
    model = ToDoTbl
    template_name = 'todo/todo.html'
    context_object_name = "objects"

    def post(self, *args, **kwargs):
        
        # Object creation.
        form = ToDoForm(self.request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

        queryset = self.model.objects.all()

        return render(self.request, 'todo/todo.html', {'objects': queryset})
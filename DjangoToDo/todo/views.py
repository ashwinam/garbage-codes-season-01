from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
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
    
class ToDoUpdateView(UpdateView):
    model = ToDoTbl
    template_name = 'todo/todo.html'
    context_object_name = "objects"
    form_class = ToDoForm
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('todos')

    def form_valid(self, form):
        todo = form.save(commit=False)
        todo.save()
        return super().form_valid(form)
    
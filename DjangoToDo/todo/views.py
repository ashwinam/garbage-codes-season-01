from typing import Any
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
    form_class = ToDoForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        try:
            kwargs['form'] = ToDoForm()
            print(kwargs['form'])
        except Exception as e:
            print(e, 'Errorrrr')
        return super(ToDoView, self).get_context_data(**kwargs)

    def post(self, *args, **kwargs):
        
        # Object creation.
        form = ToDoForm(self.request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

        queryset = self.model.objects.all()

        return render(self.request, 'todo/todo.html', {'objects': queryset, 'form': ToDoForm()})

    
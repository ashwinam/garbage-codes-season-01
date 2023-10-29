from typing import Any
from django.shortcuts import render, get_object_or_404
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
        except Exception as e:
            print(e, 'Errorrrr')
        return super(ToDoView, self).get_context_data(**kwargs)

    def post(self, *args, **kwargs):
        action = self.request.POST.get('action', None)
        todo_id = self.request.POST.get('todo_id', None)

        if action == 'create_todo':
            # Object creation.
            form = ToDoForm(self.request.POST)
            if form.is_valid():
                form.save()
            else:
                print(form.errors)

            queryset = self.model.objects.all()

            return render(self.request, 'todo/todo.html', {'objects': queryset, 'form': ToDoForm()})
        elif action == 'fetch_todo':
            if todo_id:
                obj = get_object_or_404(ToDoTbl, pk=todo_id)
                context = {
                    'todo_id': obj.todo_id,
                    'todo_name': obj.todo_name,
                    'todo_description': obj.todo_description,
                    'action': 'edit_todo',
                    'form': ToDoForm(instance=obj),
                    'objects': ToDoTbl.objects.all()
                }

            return render(self.request, 'todo/todo.html', context=context)
        else:
            return render(self.request, 'todo/todo.html', {'form': ToDoForm()})
    
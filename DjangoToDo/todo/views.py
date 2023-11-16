from typing import Any
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from .models import ToDoTbl
from .forms import ToDoForm

# Create your views here.

class index(TemplateView):
    template_name = 'base.html'

class ToDoView(LoginRequiredMixin, ListView):
    model = ToDoTbl
    template_name = 'todo/todo.html'
    context_object_name = "objects"
    form_class = ToDoForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        try:
            kwargs['form'] = ToDoForm()
            kwargs['objects'] = self.model.objects.filter(add_by=self.request.user.id)
        except Exception as e:
            print(e, 'Errorrrr')
        return super(ToDoView, self).get_context_data(**kwargs)

    def post(self, *args, **kwargs):
        action = self.request.POST.get('action', None)
        todo_id = self.request.POST.get('todo_id', None)
        if todo_id:
            obj = get_object_or_404(ToDoTbl, pk=todo_id)


        if action == 'create_todo':
            # Object creation.
            form = ToDoForm(self.request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.add_by = self.request.user.id
                form.save()
                messages.success(self.request, 'ToDo added successfully')
                queryset = self.model.objects.all()

                return render(self.request, 'todo/todo.html', {'objects': queryset, 'form': ToDoForm()})
            else:
                error_msg = ''
                for field, errors in form.errors.items():
                    error_msg += f'{field}: {",".join(errors)}'
                messages.error(self.request, error_msg)
                queryset = self.model.objects.all()

                return render(self.request, 'todo/todo.html', {'objects': queryset, 'form': ToDoForm(self.request.POST)})
            
        elif action == 'fetch_todo':
            if obj:
                context = {
                    'todo_id': obj.todo_id,
                    'todo_name': obj.todo_name,
                    'todo_description': obj.todo_description,
                    'action': 'edit_todo',
                    'form': ToDoForm(instance=obj),
                    'objects': ToDoTbl.objects.all()
                }

            return render(self.request, 'todo/todo.html', context=context)
        elif action == 'edit_todo':
            if obj:
                form = ToDoForm(data=self.request.POST, instance=obj)
                if form.is_valid():
                    form.save()

                    messages.success(self.request, 'ToDo updated successfully.')

                    return render(self.request, self.template_name, {'objects': ToDoTbl.objects.all(), 'form': self.form_class()})
                else:
                    error_msg = ''
                    for field, errors in form.errors.items():
                        error_msg += f'{field}: {",".join(errors)}'
                    messages.error(self.request, error_msg)
                    return render(self.request, 'todo/todo.html', {'objects': ToDoTbl.objects.all(), 'form': ToDoForm(self.request.POST)})
        elif action == 'delete_todo':
            if obj:
                obj.delete()
                messages.success(self.request, 'ToDo has been deleted successfully.')
                return render(self.request, self.template_name, {'objects': ToDoTbl.objects.all(), 'form': self.form_class()})
            else:
                return render(self.request, 'todo/todo.html', {'form': ToDoForm()})
        else:
            return render(self.request, 'todo/todo.html', {'form': ToDoForm()})
    
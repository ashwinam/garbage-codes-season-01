from typing import Any
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import redirect, render, get_object_or_404
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
    form_class = ToDoForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        try:
            kwargs['form'] = ToDoForm()
            objects = self.model.objects.filter(add_by=self.request.user.id)
            page = self.request.GET.get('page', 1)
            search_inp = self.request.GET.get('search_todo', '').strip()
            if search_inp:
                objects = self.model.objects.filter(add_by=self.request.user.id, todo_name__icontains=search_inp)
                kwargs['search_inp'] = search_inp
            paginate = Paginator(objects, 1)
            kwargs['objects'] = paginate.get_page(page)
            kwargs['current_page'] = kwargs['objects'].number
            
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
                form.add_by = self.request.user
                form.save()
                messages.success(self.request, 'ToDo added successfully')
                queryset = self.model.objects.filter(add_by=self.request.user)

                paginate = Paginator(queryset, 1)

                return render(self.request, 'todo/todo.html', {'objects': paginate.get_page(1), 'form': ToDoForm()})
            else:
                error_msg = ''
                for field, errors in form.errors.items():
                    error_msg += f'{field}: {",".join(errors)}'
                messages.error(self.request, error_msg)
                queryset = self.model.objects.filter(add_by=self.request.user)

                paginate = Paginator(queryset, 1)

                return render(self.request, 'todo/todo.html', {'objects': paginate.get_page(1), 'form': ToDoForm(self.request.POST)})
            
        elif action == 'fetch_todo':
            if obj:
                queryset = self.model.objects.filter(add_by=self.request.user)
                paginate = Paginator(queryset, 1)
                context = {
                    'todo_id': obj.todo_id,
                    'todo_name': obj.todo_name,
                    'todo_description': obj.todo_description,
                    'action': 'edit_todo',
                    'form': ToDoForm(instance=obj),
                    'objects': paginate.get_page(1)
                }

            return render(self.request, 'todo/todo.html', context=context)
        elif action == 'edit_todo':
            if obj:
                form = ToDoForm(data=self.request.POST, instance=obj)
                if form.is_valid():
                    form.save()

                    messages.success(self.request, 'ToDo updated successfully.')
                    
                    queryset = self.model.objects.filter(add_by=self.request.user)
                    paginate = Paginator(queryset, 1)

                    return render(self.request, self.template_name, {'objects': paginate.get_page(1), 'form': self.form_class()})
                else:
                    error_msg = ''
                    for field, errors in form.errors.items():
                        error_msg += f'{field}: {",".join(errors)}'
                    messages.error(self.request, error_msg)

                    queryset = self.model.objects.filter(add_by=self.request.user)
                    paginate = Paginator(queryset, 1)

                    return render(self.request, 'todo/todo.html', {'objects': paginate.get_page(1), 'form': ToDoForm(self.request.POST), 'action': 'edit_todo', 'todo_id': obj.todo_id})
        elif action == 'delete_todo':
            if obj:
                obj.delete()
                messages.success(self.request, 'ToDo has been deleted successfully.')

                queryset = self.model.objects.filter(add_by=self.request.user)
                paginate = Paginator(queryset, 1)

                return render(self.request, self.template_name, {'objects': paginate.get_page(1), 'form': self.form_class()})
            else:
                return render(self.request, 'todo/todo.html', {'form': ToDoForm()})
        else:
            return render(self.request, 'todo/todo.html', {'form': ToDoForm()})
    
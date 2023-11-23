from typing import Any
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models.query import QuerySet
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from .models import ToDoTbl
from .forms import ToDoForm
import traceback

# Create your views here.

class index(TemplateView):
    template_name = 'base.html'

class ToDoView(LoginRequiredMixin, ListView):
    model = ToDoTbl
    template_name = 'todo/todo.html'
    form_class = ToDoForm
    __COUNTS = 3

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        try:
            kwargs['form'] = ToDoForm()
            objects = self.model.objects.filter(add_by=self.request.user.id)
            page = self.request.GET.get('page', 1)
            search_inp = self.request.GET.get('search_todo', '').strip()
            if search_inp:
                objects = self.get_queryset(search_inp)
                kwargs['search_inp'] = search_inp
                kwargs['objects'] = self.paginator_obj(page, objects)
            else:
                kwargs['objects'] = self.paginator_obj(page)
            kwargs['current_page'] = kwargs['objects'].number
            
        except Exception as e:
            print(e, 'Errorrrr')
        
        return super(ToDoView, self).get_context_data(**kwargs)

    def post(self, *args, **kwargs):
        action = self.request.POST.get('action', None)
        todo_id = self.request.POST.get('todo_id', None)
        print(action, 'action --')
        if todo_id:
            obj = get_object_or_404(ToDoTbl, pk=todo_id)


        if action == 'create_todo':
            # Object creation.
            self.request.POST = self.request.POST.copy()
            self.request.POST['user'] = self.request.user
            form = ToDoForm(data=self.request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.add_by = self.request.user
                form.save()
                messages.success(self.request, 'ToDo added successfully')

                return render(self.request, 'todo/todo.html', {'objects': self.paginator_obj(1), 'form': ToDoForm(), 'current_page': self.paginator_obj(1).number})
            else:
                error_msg = ''
                for field, errors in form.errors.items():
                    error_msg += f'{field}: {",".join(errors)}'
                messages.error(self.request, error_msg)

                return render(self.request, 'todo/todo.html', {'objects': self.paginator_obj(1), 'form': ToDoForm(self.request.POST), 'current_page': self.paginator_obj(1).number})
            
        elif action == 'fetch_todo':
            if obj:
                context = {
                    'todo_id': obj.todo_id,
                    'todo_name': obj.todo_name,
                    'todo_description': obj.todo_description,
                    'action': 'edit_todo',
                    'form': ToDoForm(instance=obj),
                    'objects': self.paginator_obj(1),
                    'current_page': self.paginator_obj(1).number
                }

            return render(self.request, 'todo/todo.html', context=context)
        elif action == 'edit_todo':
            if obj:
                self.request.POST = self.request.POST.copy()
                self.request.POST['user'] = self.request.user
                form = ToDoForm(data=self.request.POST, instance=obj)
                if form.is_valid():
                    form.save()

                    messages.success(self.request, 'ToDo updated successfully.')

                    return render(self.request, self.template_name, {'objects': self.paginator_obj(1), 'form': self.form_class(), 'current_page': self.paginator_obj(1).number})
                else:
                    error_msg = ''
                    for field, errors in form.errors.items():
                        error_msg += f'{field}: {",".join(errors)}'
                    messages.error(self.request, error_msg)

                    return render(self.request, 'todo/todo.html', {'objects': self.paginator_obj(1), 'form': ToDoForm(self.request.POST), 'action': 'edit_todo', 'todo_id': obj.todo_id, 'current_page': self.paginator_obj(1).number})
        elif action == 'delete_todo':
            if obj:
                obj.delete()
                messages.success(self.request, 'ToDo has been deleted successfully.')

                return render(self.request, self.template_name, {'objects': self.paginator_obj(1), 'form': self.form_class(), 'current_page': self.paginator_obj(1).number})
            else:
                return render(self.request, 'todo/todo.html', {'form': ToDoForm()})
        elif action == 'change_status':
            todo_id = self.request.POST.get('id', None)
            try:
                obj = get_object_or_404(self.model, pk=todo_id)
                if obj:
                    if obj.status == 'In Progress':
                        obj.status = 'Complete'
                        obj.save()
                        return JsonResponse({'code': 'success', 'message': 'Status change successfully'}, status=200)
                    elif obj.status == 'Complete':
                        obj.status = 'In Progress'
                        obj.save()
                        return JsonResponse({'code': 'success', 'message': 'Status change successfully'}, status=200)
                else:
                    return JsonResponse({'code': 'error', 'message': "Something went wrong!"}, status=200)
            except Exception as e:
                return JsonResponse({'code': 'error', 'message': "Something went wrong!"})
        else:
            return render(self.request, 'todo/todo.html', {'form': ToDoForm()})
    
    def paginator_obj(self, page_number, queryset=None):
        if not queryset:
            queryset=self.get_queryset()
        paginate = Paginator(queryset, self.__COUNTS)
        return paginate.get_page(page_number)
    
    def get_queryset(self, search_query='') -> QuerySet[Any]:
        objects = self.model.objects.filter(add_by=self.request.user, todo_name__icontains=search_query).order_by('todo_name')
        return objects
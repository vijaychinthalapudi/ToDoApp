from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Todo

# Create your views here.
def todo_list(request):
    todos= Todo.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})

def todo_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        Todo.objects.create(title=title, description=description)
        return redirect('todo_list')
    return render(request, 'todo_form.html')

def todo_update(request, id):
    todo = get_object_or_404(Todo, id=id)

    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description', '')
        todo.completed = request.get('completed') == 'on'
        todo.save()
        return redirect('todo_list')
    return render(request, 'todo_form.html', {'todo': todo})

def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('todo_list')
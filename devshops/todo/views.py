from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Todo, Todo1
from .forms import TodoForm, TodoForm1

def index(request):
    todo_list = Todo.objects.order_by('id')
    form = TodoForm()

    todo_list1 = Todo1.objects.order_by('id')
    form1 = TodoForm1()

    context = {'todo_list' : todo_list, 'form' : form, 'todo_list1' : todo_list1, 'form1' : form1}

    return render(request, 'todo/index.html', context)

@require_POST
def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()

    return redirect('index')

def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')

def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')

def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('index')

#-----------------------------------------------------------------

@require_POST
def addTodo1(request):
    form = TodoForm1(request.POST)

    if form.is_valid():
        new_todo = Todo1(text=request.POST['text'])
        new_todo.save()

    return redirect('index')

def completeTodo1(request, todo_id):
    todo = Todo1.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('index')

def deleteCompleted1(request):
    Todo1.objects.filter(complete__exact=True).delete()
    return redirect('index')

def deleteAll1(request):
    Todo1.objects.all().delete()

    return redirect('index')

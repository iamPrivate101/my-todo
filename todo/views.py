from multiprocessing import context
from django.http import Http404
from django.shortcuts import redirect, render

from templates.todo.form import TodoForm
from .models import Todo
from django.contrib import messages

# Create your views here.
def todo_list(request):
    context =dict()
    context['todos'] = Todo.objects.all() #creating dictionary to pass all obj of Todo model
    return render(request,"todo/todo_list.html",context)


def todo_detail(request,pk):
    context = dict()
    try:
        context['todo'] = Todo.objects.get(id = pk)
    except Todo.DoesNotExist:
        raise Http404

    return render(request,'todo/todo_detail.html', context)


def todo_create(request):
    context = dict()
    if request.method == "GET":
        context["form"] = TodoForm()
        print("Get Method")
        return render(request,"todo/todo_create.html",context)
    form = TodoForm(request.POST)
    if form.is_valid():
        form.save()
        context["message"] = messages.success(request,"Inserted Successfully")
        return redirect("/")
    context['form'] = form
    return render(request,"todo/todo_create.html",context)


def todo_delete(request,pk):
    context = dict()
    try:
        todo = Todo.objects.get(id = pk)
        todo.delete()
        context["message"] = messages.success(request,"Item Deleted Successfully")
    except Todo.DoesNotExist:
        context["message"] = messages.error("Item Doesnt Exist")
    return redirect("/")

from multiprocessing import context
from django.http import Http404
from django.shortcuts import render
from .models import Todo

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
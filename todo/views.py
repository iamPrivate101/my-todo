
from django.http import Http404
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .form import TodoForm
from .models import Todo
from django.contrib import messages
from django.db.models import Q #for searching

def index(request):
    return render(request,'todo/index.html')

# Create your views here.
@login_required
def todo_list(request):
    context =dict()
    userid = request.user
    #for searching
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(title__icontains=q) | Q(is_completed__icontains=q))
        context["todos"] = Todo.objects.filter(multiple_q , user = userid)
    #end searching
    else:
        context['todos'] = Todo.objects.filter(user = userid) #creating dictionary to pass all obj of Todo model
    return render(request,"todo/todo_list.html",context)

@login_required
def todo_detail(request,pk):
    context = dict()
    try:
        context['todo'] = Todo.objects.get(id = pk)
    except Todo.DoesNotExist:
        raise Http404

    return render(request,'todo/todo_detail.html', context)

@login_required
def todo_create(request):
    context = dict()
    if request.method == "GET":
        context["form"] = TodoForm()
        print("Get Method")
        return render(request,"todo/todo_create.html",context)
    
    form = TodoForm(request.POST)
    if (form.is_valid()):
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()
        context["message"] = messages.success(request,"Inserted Successfully")
        return redirect("/")
    context['form'] = form
    return render(request,"todo/todo_create.html",context)





@login_required
def todo_delete(request,pk):
    context = dict()
    try:
        todo = Todo.objects.get(id = pk)
        todo.delete()
        context["message"] = messages.success(request,"Item Deleted Successfully")
    except Todo.DoesNotExist:
        context["message"] = messages.error("Item Doesnt Exist")
    return redirect("/")

@login_required
def todo_update(request, pk):
    context = dict()
    try:
        todo = Todo.objects.get(id = pk)
    except Todo.DoesNotExist:
        messages.error(request,"Item doesnt exist")
        return("/")
    
    if request.method == "GET":
        context["form"] = TodoForm(instance = todo)
        return render(request, "todo/todo_update.html", context)
    
    form = TodoForm(request.POST)
    if form.is_valid():
        todo.title = form.cleaned_data.get('title')
        todo.is_completed = form.cleaned_data.get('is_completed')
        todo.description = form.cleaned_data.get('description')
        todo.save()
        messages.success(request,"Todo Sucessfully Updated")
        return redirect('/')
    context['form'] = form
    return render(request, "todo/todo_update.html", context)

    

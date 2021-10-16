from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm
def index(request):
    return render(request,"todoapp/index.html")

def about(request):
    return render(request,"todoapp/about.html")

def create(request):
    if request.method=="POST":
        form=TodoForm(request.POST or None)
        if form.is_valid:
            form.save()
            return render(request, "todoapp/createtodo.html")
    else:
        return render(request,"todoapp/createtodo.html")

def delete(request,Todo_id):
    todo=Todo.objects.get(pk=Todo_id)
    todo.delete()
    return redirect("listeler")


def listeler(request):
    todo_list=Todo.objects.all()
    print(todo_list)
    return render(request,"todoapp/listeler.html",{"todo_list":todo_list})




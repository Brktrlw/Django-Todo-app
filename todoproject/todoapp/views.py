from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    a={"ad":"berkay","soyad":"şen"}
    return render(request,"todoapp/index.html",a)

def about(request):
    return render(request,"todoapp/about.html")

def create(request):
    return render(request,"todoapp/createtodo.html")

def listeler(request):
    return render(request,"todoapp/listeler.html")


from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>naber</h1>")

def about(request):
    return HttpResponse("hakkımda")


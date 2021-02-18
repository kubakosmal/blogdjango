from django.http import  HttpResponse
from django.shortcuts import render

def about(request):
    return render(request, "about.html")
    #return HttpResponse('hello')

def index(request):
    return render(request, "index.html")
    #return HttpResponse('home')
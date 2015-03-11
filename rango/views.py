from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse("Rango says hola, this is the about page")

def index(request):
    return HttpResponse("Rango says hey there world!")

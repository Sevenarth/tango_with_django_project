from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Rango says hey there partner! Go to <a href=\"/rango/about\">about page</a>!")

def about(request):
    return HttpResponse("Rango says this is the about page!")

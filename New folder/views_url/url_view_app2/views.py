from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_func(request):
    return HttpResponse("<h1> This is the home page </h1>")

def about_func(request):
    return HttpResponse("<h1> This is the about page </h1>")

def sample_func(request):
    return HttpResponse("<h1> This is the sample page </h1>")



from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    my_dict = {'insert_var' : "This is from application's view.py !"}
    return render(request , 'app_1/index.html' , context=my_dict)







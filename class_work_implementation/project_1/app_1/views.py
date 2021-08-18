import app_1
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2> Sounds good </h2>")
#     help_dict = {'help_insert' : 'This is the HELP page'}
#     return render(request, 'app_1/help.html' , context=help_dict)

# def index(request):
#    return render(request , 'app_1/index.html')
    

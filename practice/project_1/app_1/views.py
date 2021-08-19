from django.shortcuts import render
from django.http import HttpResponse
from app_1.models import users

def index(request): ## Home page
    return render(request , 'app_1/index.html') 

def users_view(request):  ## Users page
    user_lists = users.objects.order_by('first_name')
    users_dict = { 'user_records':user_lists }
    return render(request , 'app_1/users_page.html' , context=users_dict)

    

    

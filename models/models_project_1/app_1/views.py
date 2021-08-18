from django.shortcuts import render
from django.http import HttpResponse
from app_1.models import Topic,Webpage,AccessRecord

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict     = { 'access_records':webpages_list }
    return render(request , 'app_1/index.html' , context=date_dict)

    

    

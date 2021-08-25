from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'Name':'prashanth S',
                    'Age':21,
                    'Area_of_interest':'Machine Learning'}

    return render(request,'app_1/index.html',context_dict)

def other(request):
    return render(request,'app_1/other.html')

def relative(request):
    return render(request,'app_1/relative_urls_templates.html')

    
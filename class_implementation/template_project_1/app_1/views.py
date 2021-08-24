from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'app_1/index.html')
    ## will return what is inside templates directory

def other(request):
    return render(request,'app_1/other.html')

def relative(request):
    return render(request,'app_1/relative_urls_templates.html')

    
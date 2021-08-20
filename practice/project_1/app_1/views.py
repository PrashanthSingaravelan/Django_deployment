from django.shortcuts import render
from app_1.forms import newuser

def index(request):          ## Home page
    return render(request , 'app_1/index.html') 

def acceptance_page(request): ## Acceptance page
    return render(request , 'app_1/acceptance_page.html') 

def users_view(request):  ## Users page
    form = newuser()
    if (request.method == 'POST'):
        form = newuser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return acceptance_page(request)
        else:
            print("Error form is not valid")
    return render(request,'app_1/users_page.html',{'form':form})
    

    


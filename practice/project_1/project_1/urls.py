from django.conf.urls import url,include
from app_1 import views
from django.contrib import admin

urlpatterns = [
    url(r'^$'      , views.index , name='index'), 
    url(r'^users/' , include('app_1.urls')),
    url(r'^admin/' , admin.site.urls),                ## for admin's page
]

                # method-1 (going straight the applications's view page)
# url(r'^users/' , views.users , name = "users"),   ## for user's page

                # method-2 (going to application's url and then to view page)
# url(r'^users/' , include('app_1.urls')),


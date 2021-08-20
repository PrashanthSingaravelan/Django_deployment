from django.conf.urls import url
from django.conf.urls import include
from app_1 import views
from django.contrib import admin

urlpatterns = [
    url(r'^$'       , views.index , name='index'),   ## https://www.facebook.com/
    url(r'^app_1/' , include('app_1.urls')),  ## https://www.facebook.com/sprashanth.singaravelan/
    url(r'^admin/'  , admin.site.urls),
]

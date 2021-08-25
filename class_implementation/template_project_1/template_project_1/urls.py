from django.contrib import admin
from django.conf.urls import include, url
from app_1 import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'admin/', admin.site.urls),
    url(r'^app_1/' , include('app_1.urls'))
]

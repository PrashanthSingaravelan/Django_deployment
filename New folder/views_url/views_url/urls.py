from django.contrib import admin
from django.contrib import admin
from django.conf.urls import url, include
from url_view_app1 import views

urlpatterns = [
    url(r'^$', views.home_func),
    url(r'^app1/',include('url_view_app1.urls')),
    url(r'^app2/',include('url_view_app2.urls')),
    url(r'^admin/', admin.site.urls),
]

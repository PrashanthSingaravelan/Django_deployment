from django.urls import path
from django.conf.urls import url
from url_view_app1 import views

urlpatterns = [
    url(r'^$', views.home_func),
    path('about_page',views.about_func),
    path('sample_page',views.sample_func)
]

from django.conf.urls import url
from app_1 import views

urlpatterns = [
    url(r'^$' , views.index , name='index'),
]

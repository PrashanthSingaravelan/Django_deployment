from django.conf.urls import url
from app_1 import views

app_name = 'app_1'

urlpatterns = [
    url(r'^register/$',views.register,name='register')
]


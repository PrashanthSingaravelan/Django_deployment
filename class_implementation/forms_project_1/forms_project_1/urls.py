from django.conf.urls import url
from django.contrib import admin
from app_1 import views

urlpatterns = [
    url(r'^$'         , views.index,          name='index'),
    url(r'^form_page/', views.form_name_view, name='form_name'),
    url(r'^admin/'    , admin.site.urls)
]

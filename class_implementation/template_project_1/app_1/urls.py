from django.conf.urls import url
from app_1 import views

## template_tagging
app_name = 'app_1' ## Look the under the app_1 and find the url that matches

    # 1) domain_name/app_1/relative --> gives the relative view
    # 2) domain_name/app_1/other    --> gives the other view
urlpatterns = [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',   views.other,   name='other')
]



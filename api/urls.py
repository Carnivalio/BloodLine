from django.conf.urls import  include, url
from api import views

urlpatterns = [
    url(r'^getUserList/$', views.getUserList),
    url(r'^setUser/$', views.setUser),
]
from django.conf.urls import url

from . import views

app_name = 'bloodline'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='user_detail'),
    url(r'^user_create/$', views.CreateUser.as_view(), name='user_create'),
    url(r'^(?P<pk>\d+)/user_update/$', views.UpdateUser.as_view(), name='user_update'),
    url(r'^(?P<pk>\d+)/user_delete/$', views.DeleteUser.as_view(), name='user_delete'),
]
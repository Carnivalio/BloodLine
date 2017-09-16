from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from .models import BloodlineUser, BloodlineBank, BloodlineBlood

from . import views
from . import user_views

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BloodlineUser
        # fields = ('url', 'username', 'email', 'is_staff')
        fields = ('username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = BloodlineUser.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

app_name = 'bloodline'
urlpatterns = [
    # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^rest/', include(router.urls)),
    # url(r'^', include(router.urls)),
    url(r'^$', views.home, name='home'),
    url(r'^(?P<pk>[0-9]+)/$', user_views.DetailView.as_view(), name='user_detail'),
    url(r'^user_create/$', user_views.CreateUser.as_view(), name='user_create'),
    url(r'^(?P<pk>\d+)/user_update/$', user_views.UpdateUser.as_view(), name='user_update'),
    url(r'^(?P<pk>\d+)/user_delete/$', user_views.DeleteUser.as_view(), name='user_delete'),
    url(r'^login/$', auth_views.login, {'template_name': 'bloodline/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'bloodline_app:login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
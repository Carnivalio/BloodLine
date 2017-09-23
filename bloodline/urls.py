from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from bloodline.models import BloodlineUser, BloodlineBank, BloodlineBlood

from bloodline import views
from bloodline import user_views

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'


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
    url(r'^header/', views.header),
    url(r'^base-search/', views.base_search),

    url(r'^(?P<pk>[0-9]+)/$', user_views.DetailView.as_view(), name='user_detail'),
    url(r'^user_create/$', user_views.CreateUser.as_view(), name='user_create'),
    url(r'^(?P<pk>\d+)/user_update/$', user_views.UpdateUser.as_view(), name='user_update'),
    url(r'^(?P<pk>\d+)/user_delete/$', user_views.DeleteUser.as_view(), name='user_delete'),
    url(r'^login/$', auth_views.login, {'template_name': 'bloodline/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'bloodline_app:login'}, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^password_reset/$', auth_views.password_reset, {'post_reset_redirect': '/bloodline/password_reset/done/','email_template_name': 'registration/password_reset_email.html'}, name='password_reset'),
    url(r'^password_reset/done/$(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, {'post_reset_redirect': '/bloodline/reset/done/'},
        name='password_reset_confirm'),
    url(r'^reset/done/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})$',
        auth_views.password_reset_complete, name='password_reset_complete'),

    # Url Entries for social auth
    url('', include('social.apps.django_app.urls', namespace='social')),

    # Url Entries for django administration
    url('', include('django.contrib.auth.urls', namespace='auth')),

    url(r'^admin/', admin.site.urls),
]

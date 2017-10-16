from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin

from django.contrib.admin.views.decorators import user_passes_test
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from bloodline.models import BloodlineUser, BloodlineBank, BloodlineBlood

from bloodline import views
from bloodline import user_views
from bloodline import bank_views
from bloodline import blood_views

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

    url(r'^staff/users/(?P<pk>\d+)/user_update/$', user_passes_test(lambda u: u.is_staff) (user_views.UpdateUser.as_view()), name='user_update'),
    url(r'^staff/users/(?P<pk>\d+)/user_delete/$', user_passes_test(lambda u: u.is_staff) (user_views.DeleteUser.as_view()), name='user_delete'),
    url(r'^staff/users/(?P<pk>\d+)/$', user_passes_test(lambda u: u.is_staff) (user_views.DetailUser.as_view()), name='user_detail'),
    url(r'^staff/users/user_create/$', user_passes_test(lambda u: u.is_staff) (user_views.CreateUser.as_view()), name='user_create'),
    url(r'^staff/users/$', user_passes_test(lambda u: u.is_staff) (user_views.UserListView.as_view()), name='user_list'),

    url(r'^staff/banks/(?P<pk>\d+)/bank_update/$', user_passes_test(lambda u: u.is_staff) (bank_views.UpdateBank.as_view()), name='bank_update'),
    url(r'^staff/banks/(?P<pk>\d+)/bank_delete/$', user_passes_test(lambda u: u.is_staff) (bank_views.DeleteBank.as_view()), name='bank_delete'),
    url(r'^staff/banks/(?P<pk>\d+)/$', user_passes_test(lambda u: u.is_staff) (bank_views.DetailBank.as_view()), name='bank_detail'),
    url(r'^staff/banks/bank_create/$', user_passes_test(lambda u: u.is_staff) (bank_views.CreateBank.as_view()), name='bank_create'),
    url(r'^staff/banks/$', user_passes_test(lambda u: u.is_staff) (bank_views.BankListView.as_view()), name='bank_list'),

    url(r'^staff/bloods/(?P<pk>\d+)/blood_update/$', user_passes_test(lambda u: u.is_staff) (blood_views.UpdateBlood.as_view()), name='blood_update'),
    url(r'^staff/bloods/(?P<pk>\d+)/blood_delete/$', user_passes_test(lambda u: u.is_staff) (blood_views.DeleteBlood.as_view()), name='blood_delete'),
    url(r'^staff/bloods/(?P<pk>\d+)/$', user_passes_test(lambda u: u.is_staff) (blood_views.DetailBlood.as_view()), name='blood_detail'),
    url(r'^staff/bloods/blood_create/$', user_passes_test(lambda u: u.is_staff) (blood_views.CreateBlood.as_view()), name='blood_create'),
    url(r'^staff/bloods/$', user_passes_test(lambda u: u.is_staff) (blood_views.BloodListView.as_view()), name='blood_list'),

    url(r'^staff/', views.staff_main, name='staff_main'),

    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'bloodline_app:login'}, name='logout'),
    url(r'^appointment/$', views.appointment, name='appointment'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^list_centre/$',views.list_centre, name='list_centre'),
    url(r'^password_reset/$', auth_views.password_reset, {'post_reset_redirect': '/bloodline/password_reset/done/','email_template_name': 'registration/password_reset_email.html'}, name='password_reset'),
    url(r'^password_reset/done/$(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, {'post_reset_redirect': '/bloodline/reset/done/'},
        name='password_reset_confirm'),
    url(r'^reset/done/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})$',
        auth_views.password_reset_complete, name='password_reset_complete'),

    # Url Entries for social auth
    # url('', include('social.apps.django_app.urls', namespace='social')),

    # Url Entries for django administration
    # url('', include('django.contrib.auth.urls', namespace='auth')),

    # url('', views.index2),
    url(r'^index2/', views.index2),

    url(r'^admin/', admin.site.urls),
]

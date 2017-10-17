from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.admin.views.decorators import user_passes_test
from django.contrib.auth import views as auth_views
from rest_framework import routers, serializers, viewsets

from . import bank_views, blood_views, user_views, views
from .models import BloodlineUser

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BloodlineUser
        fields = ('id', 'username', 'first_name', 'last_name', 'gender', 'blood_type')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = BloodlineUser.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

app_name = 'bloodline'
urlpatterns = [
    url(r'^staff/users/(?P<pk>\d+)/user_update/$',
        user_passes_test(lambda u: u.is_staff)(user_views.UpdateUser.as_view()), name='user_update'),
    url(r'^staff/users/(?P<pk>\d+)/user_delete/$',
        user_passes_test(lambda u: u.is_staff)(user_views.DeleteUser.as_view()), name='user_delete'),
    url(r'^staff/users/(?P<pk>\d+)/$', user_passes_test(lambda u: u.is_staff)(user_views.DetailUser.as_view()),
        name='user_detail'),
    url(r'^staff/users/user_create/$', user_passes_test(lambda u: u.is_staff)(user_views.CreateUser.as_view()),
        name='user_create'),
    url(r'^staff/users/$', user_passes_test(lambda u: u.is_staff)(user_views.UserListView.as_view()), name='user_list'),

    url(r'^staff/banks/(?P<pk>\d+)/bank_update/$',
        user_passes_test(lambda u: u.is_staff)(bank_views.UpdateBank.as_view()), name='bank_update'),
    url(r'^staff/banks/(?P<pk>\d+)/bank_delete/$',
        user_passes_test(lambda u: u.is_staff)(bank_views.DeleteBank.as_view()), name='bank_delete'),
    url(r'^staff/banks/(?P<pk>\d+)/$', user_passes_test(lambda u: u.is_staff)(bank_views.DetailBank.as_view()),
        name='bank_detail'),
    url(r'^staff/banks/bank_create/$', user_passes_test(lambda u: u.is_staff)(bank_views.CreateBank.as_view()),
        name='bank_create'),
    url(r'^staff/banks/$', user_passes_test(lambda u: u.is_staff)(bank_views.BankListView.as_view()), name='bank_list'),

    url(r'^staff/bloods/(?P<pk>\d+)/blood_update/$',
        user_passes_test(lambda u: u.is_staff)(blood_views.UpdateBlood.as_view()), name='blood_update'),
    url(r'^staff/bloods/(?P<pk>\d+)/blood_delete/$',
        user_passes_test(lambda u: u.is_staff)(blood_views.DeleteBlood.as_view()), name='blood_delete'),
    url(r'^staff/bloods/(?P<pk>\d+)/$', user_passes_test(lambda u: u.is_staff)(blood_views.DetailBlood.as_view()),
        name='blood_detail'),
    url(r'^staff/bloods/blood_create/$', user_passes_test(lambda u: u.is_staff)(blood_views.CreateBlood.as_view()),
        name='blood_create'),
    url(r'^staff/bloods/$', user_passes_test(lambda u: u.is_staff)(blood_views.BloodListView.as_view()),
        name='blood_list'),

    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'bloodline_app:login'}, name='logout'),
    url(r'^login/$', auth_views.login, {'template_name': 'bloodline/registration/login.html'}, name='login'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate,
        name='activate'),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^list_centre$', views.list_centre, name='list_centre'),
    url(r'^list_blood$', views.list_blood, name='list_blood'),
    url(r'^appointment/$', blood_views.CreateBloodPublic.as_view(), name='appointment'),

    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, {'post_reset_redirect': '/bloodline/reset/done/'}, name='password_reset_confirm'),
    url(r'^password_reset/$', auth_views.password_reset, {'post_reset_redirect': '/bloodline/password_reset/done/', 'email_template_name': 'bloodline/registration/password_reset_email.html'}, name='password_reset'),

    url(r'^staff/', views.staff_main, name='staff_main'),
    url(r'^admin/', admin.site.urls),

    url(r'^api/', include(router.urls)),
    url(r'^header/', views.header),
    url(r'^base-search/', views.base_search),

    url(r'^$', views.home, name='home'),
]

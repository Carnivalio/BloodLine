"""urls.py

This module mostly handle the routing of the application

Variables:
	LOGIN_URL {str} -- provide default login route name
	LOGOUT_URL {str} -- provide default logout route name
	LOGIN_REDIRECT_URL {str} -- provide default login redirect route name
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.admin.views.decorators import user_passes_test
from django.contrib.auth import views as auth_views
from rest_framework import routers, serializers, viewsets

from . import bank_views, blood_views, user_views, views
from .models import BloodlineUser, BloodlineBank, BloodlineBlood

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'

# Serializers define the API representation for User.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BloodlineUser
        fields = ('id', 'username', 'first_name', 'last_name', 'gender', 'blood_type')

# Serializers define the API representation for Blood Bank.
class BankSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BloodlineBank
        fields = ('id', 'name', 'address', 'postcode', 'phone', 'email')

# Serializers define the API representation for Blood Donation.
class BloodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BloodlineBlood
        fields = ('id', 'user', 'bank', 'donation_choice', 'donor_date', 'blood_status')

# ViewSets define the view behavior for BloodlineUser object.
class UserViewSet(viewsets.ModelViewSet):
    queryset = BloodlineUser.objects.all()
    serializer_class = UserSerializer

# ViewSets define the view behavior for BloodlineBank object.
class BankViewSet(viewsets.ModelViewSet):
    queryset = BloodlineBank.objects.all()
    serializer_class = BankSerializer

# ViewSets define the view behavior for BloodlineBlood object.
class BloodViewSet(viewsets.ModelViewSet):
    queryset = BloodlineBlood.objects.all()
    serializer_class = BloodSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

# Register ViewSets classes to urls type
router.register(r'users', UserViewSet)
router.register(r'banks', BankViewSet)
router.register(r'bloods', BloodViewSet)

# Provide the classname for the project
app_name = 'bloodline'
urlpatterns = [

	# Below are administrator/staff url related to user management
    url(r'^staff/users/(?P<pk>\d+)/user_update/$',
        user_passes_test(lambda u: u.is_staff)(user_views.UpdateUser.as_view()), name='user_update'),
    url(r'^staff/users/(?P<pk>\d+)/user_delete/$',
        user_passes_test(lambda u: u.is_staff)(user_views.DeleteUser.as_view()), name='user_delete'),
    url(r'^staff/users/(?P<pk>\d+)/$', user_passes_test(lambda u: u.is_staff)(user_views.DetailUser.as_view()),
        name='user_detail'),
    url(r'^staff/users/user_create/$', user_passes_test(lambda u: u.is_staff)(user_views.CreateUser.as_view()),
        name='user_create'),
    url(r'^staff/users/$', user_passes_test(lambda u: u.is_staff)(user_views.UserListView.as_view()), name='user_list'),

	# Below are administrator/staff url related to blood bank management
    url(r'^staff/banks/(?P<pk>\d+)/bank_update/$',
        user_passes_test(lambda u: u.is_staff)(bank_views.UpdateBank.as_view()), name='bank_update'),
    url(r'^staff/banks/(?P<pk>\d+)/bank_delete/$',
        user_passes_test(lambda u: u.is_staff)(bank_views.DeleteBank.as_view()), name='bank_delete'),
    url(r'^staff/banks/(?P<pk>\d+)/$', user_passes_test(lambda u: u.is_staff)(bank_views.DetailBank.as_view()),
        name='bank_detail'),
    url(r'^staff/banks/bank_create/$', user_passes_test(lambda u: u.is_staff)(bank_views.CreateBank.as_view()),
        name='bank_create'),
    url(r'^staff/banks/$', user_passes_test(lambda u: u.is_staff)(bank_views.BankListView.as_view()), name='bank_list'),

	# Below are administrator/staff url related to blood donation management
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

	# Below are client basic authentication and activation url
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'bloodline_app:login'}, name='logout'),
    url(r'^login/$', auth_views.login, {'template_name': 'bloodline/registration/login.html'}, name='login'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate,
        name='activate'),

    # These url provide access for AJAX to interract with the Django classes
    url(r'^list_centre$', views.list_centre, name='list_centre'),
    url(r'^list_blood$', views.list_blood, name='list_blood'),

    # This url point to the client side appointment booking
    url(r'^appointment/$', blood_views.CreateBloodPublic, name='appointment'),

    # Urls below related to password reset function
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, {'post_reset_redirect': '/bloodline/reset/done/'}, name='password_reset_confirm'),
    url(r'^password_reset/$', auth_views.password_reset, {'post_reset_redirect': '/bloodline/password_reset/done/', 'email_template_name': 'bloodline/registration/password_reset_email.html'}, name='password_reset'),

    # Urls below direct to admin/staff page (requires staff level user)
    url(r'^staff/', views.staff_main, name='staff_main'),
    url(r'^admin/', admin.site.urls),

    # Url for RESTful API
    url(r'^api/', include(router.urls)),

    # Url for html header file
    url(r'^header/', views.header),

    # Url AJAX search form
    url(r'^base-search/', views.base_search),

    # Url to direct to index/home
    url(r'^$', user_passes_test(lambda u: u.is_authenticated)(views.Home.as_view()), name='home'),
]

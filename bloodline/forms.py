from django import forms
from django.contrib.auth.forms import UserCreationForm
from datetimewidget.widgets import DateTimeWidget

from .models import BloodlineUser, BloodlineBank, BloodlineBlood

class BloodlineUserForm(UserCreationForm):
    class Meta:
        model = BloodlineUser
        fields = ['username', 'email', 'password1', 'password2', 'gender', 'first_name', 'last_name', 'mobile', 'address', 'blood_type', 'public_profile']

class BloodlineBankForm(forms.ModelForm):
    class Meta:
        model = BloodlineBank
        fields = ['name', 'address', 'phone', 'email', 'postcode']

class BloodlineBloodForm(forms.ModelForm):
    class Meta:
        model = BloodlineBlood
        fields = ['user', 'bank', 'donor_date', 'blood_status']
        widgets = {'donor_date': DateTimeWidget(attrs = {'id':'id_dateTimeField'}, bootstrap_version=3)}

# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(max_length=200, help_text='Required')

#     class Meta:
#         model = BloodlineUser
#         fields = ['email', 'username', 'password1', 'password2', 'gender', 'first_name', 'last_name', 'mobile', 'address', 'blood_type', 'verified', 'is_staff', 'is_active', 'is_superuser']

class PasswordResetRequestForm(forms.Form):
    email_or_username = forms.CharField(label=("Email Or Username"), max_length=254)

class ForgetPwdForm(forms.Form):
    email = forms.EmailField(required=True)

class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=6)
    password2 = forms.CharField(required=True, min_length=6)

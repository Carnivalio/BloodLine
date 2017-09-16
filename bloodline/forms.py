from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import BloodlineUser, BloodlineBank, BloodlineBlood

class BloodlineUserForm(UserCreationForm):
    class Meta:
        model = BloodlineUser
        fields = ['email', 'username', 'password1', 'password2', 'gender', 'first_name', 'last_name', 'mobile', 'address', 'blood_type', 'verified', 'is_staff', 'is_active', 'is_superuser']

class BloodlineBankForm(forms.ModelForm):
    class Meta:
        model = BloodlineBank
        fields = ['name', 'address', 'phone', 'email', 'user']

class BloodlineBloodForm(forms.ModelForm):
    class Meta:
        model = BloodlineBlood
        fields = ['user', 'bank', 'donor_date', 'blood_status']

class SignUpForm(UserCreationForm):
    class Meta:
        model = BloodlineUser
        fields = ['email', 'username', 'password1', 'password2', 'gender', 'first_name', 'last_name', 'mobile', 'address', 'blood_type', 'verified', 'is_staff', 'is_active', 'is_superuser']

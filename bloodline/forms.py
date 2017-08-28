from django import forms

from .models import User, Bank, Blood

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'first_name', 'last_name', 'mobile', 'address', 'blood_type', 'verified']

class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ['name', 'address', 'phone', 'email', 'user']

class BloodForm(forms.ModelForm):
    class Meta:
        model = Blood
        fields = ['user', 'bank', 'donor_date', 'blood_status']
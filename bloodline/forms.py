from django import forms
from django.contrib.auth.forms import UserCreationForm
from datetimewidget.widgets import DateTimeWidget

from .models import BloodlineUser, BloodlineBank, BloodlineBlood

class BloodlineUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(BloodlineUserForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2', 'mobile', 'address', 'blood_type']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = BloodlineUser
        fields = ['username', 'email', 'password1', 'password2', 'gender', 'first_name', 'last_name', 'mobile', 'address', 'blood_type', 'public_profile']

class BloodlineBankForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BloodlineBankForm, self).__init__(*args, **kwargs)
        for fieldname in ['name', 'address', 'postcode', 'phone', 'email']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = BloodlineBank
        fields = ['name', 'address', 'postcode', 'phone', 'email']

class BloodlineBloodForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BloodlineBloodForm, self).__init__(*args, **kwargs)
        for fieldname in ['user', 'bank', 'donation_choices','donor_date', 'blood_status']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = BloodlineBlood
        fields = ['user', 'bank', 'donation_choices', 'donor_date', 'blood_status']
        widgets = {'donor_date': DateTimeWidget(attrs = {'id':'id_dateTimeField'}, bootstrap_version=3)}

class BloodlineBloodFormPublic(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BloodlineBloodFormPublic, self).__init__(*args, **kwargs)
        for fieldname in ['bank', 'donation_choices','donor_date']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = BloodlineBlood
        fields = ['bank', 'donation_choices', 'donor_date']
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

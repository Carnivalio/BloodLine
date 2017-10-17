"""forms.py

This module provide forms for multiple occasions
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from datetimewidget.widgets import DateTimeWidget

from .models import BloodlineUser, BloodlineBank, BloodlineBlood

# This class provide the form that used for user registration process
class BloodlineUserForm(UserCreationForm):

	# This fuction is to hide the 'help text' on specific fields
    def __init__(self, *args, **kwargs):
        super(BloodlineUserForm, self).__init__(*args, **kwargs)

        # In this case username, password1, password2, mobile, address, blood_type will not show the 'help text'
        for fieldname in ['username', 'password1', 'password2', 'mobile', 'address', 'blood_type']:
            self.fields[fieldname].help_text = None

    # Child class that provide the 'shape' of the form, with fields list and the model to be used
    class Meta:
        model = BloodlineUser
        fields = ['username', 'email', 'password1', 'password2', 'gender', 'first_name', 'last_name', 'mobile', 'address', 'blood_type', 'public_profile']

# This class provide the form that used for blood bank registration process
class BloodlineBankForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BloodlineBankForm, self).__init__(*args, **kwargs)
        for fieldname in ['name', 'address', 'postcode', 'phone', 'email']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = BloodlineBank
        fields = ['name', 'address', 'postcode', 'phone', 'email']

# This class provide the form that used for blood donation (admin/staff) registration process
class BloodlineBloodForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BloodlineBloodForm, self).__init__(*args, **kwargs)
        for fieldname in ['user', 'bank', 'donation_choices','donor_date', 'blood_status']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = BloodlineBlood
        fields = ['user', 'bank', 'donation_choices', 'donor_date', 'blood_status']
        widgets = {'donor_date': DateTimeWidget(attrs = {'id':'id_dateTimeField'}, bootstrap_version=3)}

# This class provide the form that used for blood donation (public) registration process
class BloodlineBloodFormPublic(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BloodlineBloodFormPublic, self).__init__(*args, **kwargs)
        for fieldname in ['bank', 'donation_choices','donor_date']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = BloodlineBlood
        fields = ['bank', 'donation_choices', 'donor_date']
        widgets = {'donor_date': DateTimeWidget(attrs = {'id':'id_dateTimeField'}, bootstrap_version=3)}

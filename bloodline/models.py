import datetime

from django.db import models
from django.forms import ModelForm
from django.utils import timezone
from django.core.validators import RegexValidator

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Mobile/Phone number must be entered in the format: '+999999999'. Minimum 9 digits & up to 15 digits allowed.")

BLOOD_CHOICES = (
    (0, 'O'),
    (1, 'A'),
    (2, 'B'),
    (3, 'AB'),
)

STATUS_CHOICES = (
    (0, 'Received'),
    (1, 'Tested'),
    (2, 'Stored'),
    (3, 'Donated'),
)

class User(models.Model):
    email = models.EmailField(max_length=70, blank=False)
    username = models.CharField(max_length=200, null=False, blank=False, unique=True)
    password = models.CharField(max_length=200, null=False, blank=False)
    first_name = models.CharField(max_length=40, null=False, blank=False)
    last_name = models.CharField(max_length=40, null=True, blank=True)
    mobile = models.CharField(max_length=15, validators=[phone_regex], blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    blood_type = models.IntegerField(choices=BLOOD_CHOICES, default=0, null=False, blank=False)
    verified = models.BooleanField(default=False)
    def __str__(self):
        return self.username

class Bank(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False, unique=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=15, validators=[phone_regex], blank=True)
    email = models.EmailField(max_length=70, blank=False)
    user = models.ManyToManyField(User, through='Blood')
    def __str__(self):
        return self.name

class Blood(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    donor_date = models.DateTimeField('donor date', null=False, blank=False, unique=True)
    blood_status = models.IntegerField(choices=STATUS_CHOICES, default=0, null=False, blank=False)
    def __str__(self):
        # return dict(STATUS_CHOICES).get(self.blood_status)
        return self.user.username
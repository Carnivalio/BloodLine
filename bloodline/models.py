import datetime

from django.db import models
from django.forms import ModelForm
from django.utils import timezone
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Mobile/Phone number must be entered in the format: '+999999999'. Minimum 9 digits & up to 15 digits allowed.")

BLOOD_CHOICES = (
    (0, 'Not Specified'),
    (1, 'A Positive'),
    (2, 'A Negative'),
    (3, 'B Positive'),
    (4, 'B Negative'),
    (5, 'AB Positive'),
    (6, 'AB Negative'),
    (7, 'O Positive'),
    (7, 'O Negative'),
)

STATUS_CHOICES = (
    (0, 'Received'),
    (1, 'Tested'),
    (2, 'Stored'),
    (3, 'Donated'),
)

GENDER_CHOICES = (
    (0, 'Not Specified'),
    (1, 'Male'),
    (2, 'Female'),
)

class BloodlineUser(AbstractUser):
    gender = models.IntegerField(choices=GENDER_CHOICES, default=0, null=False, blank=False)
    mobile = models.CharField(max_length=15, validators=[phone_regex], null=True, blank=True, help_text="Mobile/Phone number must be entered in the format: '+999999999'. Minimum 9 digits & up to 15 digits allowed.")
    address = models.CharField(max_length=200, null=True, blank=True, help_text="Put your address here, maximum 200 characters.")
    blood_type = models.IntegerField(choices=BLOOD_CHOICES, default=0, null=False, blank=False, help_text="Make sure you selected correct blood type.")
    public_profile = models.BooleanField(default=False, help_text="Check if you want your profile to be public")
    verified = models.BooleanField(default=False, help_text="This field is to be checked by staff")

class BloodlineBank(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False, unique=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=15, validators=[phone_regex], blank=True)
    email = models.EmailField(max_length=70, blank=False)
    postcode = models.CharField(max_length=4, blank=False)
    user = models.ManyToManyField(BloodlineUser, through='BloodlineBlood')
    def __str__(self):
        return self.name

class BloodlineBlood(models.Model):
    user = models.ForeignKey(BloodlineUser, on_delete=models.CASCADE)
    bank = models.ForeignKey(BloodlineBank, on_delete=models.CASCADE)
    donor_date = models.DateTimeField('donor date', null=False, blank=False, unique=True)
    blood_status = models.IntegerField(choices=STATUS_CHOICES, default=0, null=False, blank=False)
    def __str__(self):
        # return dict(STATUS_CHOICES).get(self.blood_status)
        return self.user.username


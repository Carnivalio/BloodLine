"""models.py

This model is the 'core' of the application even though it only acts as a storage
"""

import datetime

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ModelForm
from django.template.defaulttags import register
from django.utils import timezone
from twython import Twython

# Regex codes to validate phone number, implemented in text field for client input verification
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Mobile/Phone number must be entered in the format: '+999999999'. Minimum 9 digits & up to 15 digits allowed.")

# The choice of blood type, represented with tuple to minimize the data error possibilities
BLOOD_CHOICES = (
    (0, 'Not Specified'),
    (1, 'A Positive'),
    (2, 'A Negative'),
    (3, 'B Positive'),
    (4, 'B Negative'),
    (5, 'AB Positive'),
    (6, 'AB Negative'),
    (7, 'O Positive'),
    (8, 'O Negative'),
)

# The choice of donation status, represented with tuple to minimize the data error possibilities
STATUS_CHOICES = (
    (0, 'Planned'),
    (1, 'Received'),
    (2, 'Tested'),
    (3, 'Stored'),
    (4, 'Donated'),
)

# The choice of gender, represented with tuple to minimize the data error possibilities
GENDER_CHOICES = (
    (0, 'Not Specified'),
    (1, 'Male'),
    (2, 'Female'),
)

# The choice of blood donation type, represented with tuple to minimize the data error possibilities
DONATION_CHOICES = (
    (0, 'Whole Blood'),
    (1, 'Plasma'),
    (2, 'Platelet'),
)

# Declaration of twitter object from twython library to support tweeting updates on some occassions
twitter = Twython(settings.TWITTER_APP_KEY, settings.TWITTER_APP_SECRET, settings.TWITTER_OAUTH_TOKEN, settings.TWITTER_OAUTH_TOKEN_SECRET)

# The main User database model, this model also replaced django user model for backend authentication
class BloodlineUser(AbstractUser):

	# This field store integers/numbers that represented from GENDER_CHOICES tuple
    gender = models.IntegerField(choices=GENDER_CHOICES, default=0, null=False, blank=False)
    mobile = models.CharField(max_length=15, validators=[phone_regex], null=True, blank=True, help_text="Mobile/Phone number must be entered in the format: '+999999999'. Minimum 9 digits & up to 15 digits allowed.")
    address = models.CharField(max_length=200, null=True, blank=True, help_text="Put your address here, maximum 200 characters.")
    blood_type = models.IntegerField(choices=BLOOD_CHOICES, default=0, null=False, blank=False, help_text="Make sure you selected correct blood type.")

    # This field is used for used that what themselves to be search-able on public in case of emergency
    public_profile = models.BooleanField(default=False, help_text="Check if you want your profile to be public")

    # This field is only for staff, this means the user is verified of clean and healthy blood
    verified = models.BooleanField(default=False, help_text="This field is to be checked by staff")

    # This function is the default function of user model, when user model is called without any arguments, it will return this (self.username)
    def __str__(self):
        return self.username

    # This fuction get the text version of the GENDER_CHOICES tuple from the provided index
    @register.filter
    def get_gender(self):
        return dict(GENDER_CHOICES).get(self.gender)

    # This fuction get the text version of the BLOOD_CHOICES tuple from the provided index
    @register.filter
    def get_blood_type(self):
        return dict(BLOOD_CHOICES).get(self.blood_type)

# This model stores the blood bank location information
class BloodlineBank(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False, unique=True, help_text="Put the blood bank name here, maximum 80 characters.")
    address = models.CharField(max_length=200, null=True, blank=True, help_text="Put your address here, maximum 200 characters.")
    postcode = models.CharField(max_length=4, blank=False, help_text="Postcode format: XXXX.")
    phone = models.CharField(max_length=15, validators=[phone_regex], blank=True, help_text="Mobile/Phone number must be entered in the format: '+999999999'. Minimum 9 digits & up to 15 digits allowed.")
    email = models.EmailField(max_length=70, blank=False)

    # This is the 'bridge' to connect between BloodlineBank and BloodlineUser via BloodlineBlood
    user = models.ManyToManyField(BloodlineUser, through='BloodlineBlood')

    # This function is the default function of bank model, when bank model is called without any arguments, it will return this (self.name)
    def __str__(self):
        return self.name

# This model stores the blood donation status that connects BloodlineUser and BloodlineBank
class BloodlineBlood(models.Model):
    user = models.ForeignKey(BloodlineUser, on_delete=models.CASCADE, help_text="Choose which user donated their blood.")
    bank = models.ForeignKey(BloodlineBank, on_delete=models.CASCADE, help_text="Choose which bank did the user donated their blood into.")

    # The choice of donation that will have or had given
    donation_choices = models.IntegerField(choices=DONATION_CHOICES, default=0, null=False, blank=False, help_text="Make sure you selected correct donation choice.")

    # This field is about the date when the user donates their blood
    donor_date = models.DateTimeField('donor date', null=False, blank=False, help_text="Date & time format: DD/MM/YYYY HH:MM.")

    # The status of the submitted blood related to specific user and bank
    blood_status = models.IntegerField(choices=STATUS_CHOICES, default=0, null=False, blank=False, help_text="Set the status of the donated blood.")

    # This fuction get the text version of the DONATION_CHOICES tuple from the provided index
    @register.filter
    def get_donation_choice(self):
        return dict(DONATION_CHOICES).get(self.donation_choices)

    # This fuction get the text version of the STATUS_CHOICES tuple from the provided index
    @register.filter
    def get_blood_status(self):
        return dict(STATUS_CHOICES).get(self.blood_status)

# Funtion to post/tweet on twitter everytime new user joined the Bloodline
@receiver(post_save, sender=BloodlineUser, dispatch_uid="twitter_publish_user_tag")
def twitter_publish_user(sender, instance, **kwargs):
    try:
        twitter.update_status(status='Congratulations ' + instance.username + ' for registering on BloodLineDonation, your help is very much appreciated!!!')
    except Exception as e:
        print("ERROR (TWITTER POST): " + str(e))

# Funtion to post/tweet on twitter everytime new blood bank joined the Bloodline
@receiver(post_save, sender=BloodlineBank, dispatch_uid="twitter_publish_bank_tag")
def twitter_publish_bank(sender, instance, **kwargs):
    try:
        twitter.update_status(status='Welcome aboard ' + instance.name + ', thank you for supporting BloodLineDonation by being a blood bank!!!')
    except Exception as e:
        print("ERROR (TWITTER POST): " + str(e))

# Funtion to post/tweet on twitter everytime user donated/planning to donate their blood
@receiver(post_save, sender=BloodlineBlood, dispatch_uid="twitter_publish_blood_tag")
def twitter_publish_blood(sender, instance, **kwargs):
    try:
        twitter.update_status(status=instance.user.username + ' is just being awesome by donating their blood on BloodLineDonation on ' + instance.bank.name + ' bank!!! (' + instance.donor_date.strftime('%d-%m-%Y') + ')')
    except Exception as e:
        print("ERROR (TWITTER POST): " + str(e))


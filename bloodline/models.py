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

twitter = Twython(settings.TWITTER_APP_KEY, settings.TWITTER_APP_SECRET, settings.TWITTER_OAUTH_TOKEN, settings.TWITTER_OAUTH_TOKEN_SECRET)

class BloodlineUser(AbstractUser):
    gender = models.IntegerField(choices=GENDER_CHOICES, default=0, null=False, blank=False)
    mobile = models.CharField(max_length=15, validators=[phone_regex], null=True, blank=True, help_text="Mobile/Phone number must be entered in the format: '+999999999'. Minimum 9 digits & up to 15 digits allowed.")
    address = models.CharField(max_length=200, null=True, blank=True, help_text="Put your address here, maximum 200 characters.")
    blood_type = models.IntegerField(choices=BLOOD_CHOICES, default=0, null=False, blank=False, help_text="Make sure you selected correct blood type.")
    public_profile = models.BooleanField(default=False, help_text="Check if you want your profile to be public")
    verified = models.BooleanField(default=False, help_text="This field is to be checked by staff")

    def __str__(self):
        return self.username

    @register.filter
    def get_gender(self):
        return dict(GENDER_CHOICES).get(self.gender)

    @register.filter
    def get_blood_type(self):
        return dict(BLOOD_CHOICES).get(self.blood_type)

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
    donor_date = models.DateTimeField('donor date', null=False, blank=False)
    blood_status = models.IntegerField(choices=STATUS_CHOICES, default=0, null=False, blank=False)

    @register.filter
    def get_blood_status(self):
        return dict(STATUS_CHOICES).get(self.blood_status)

@receiver(post_save, sender=BloodlineUser, dispatch_uid="twitter_publish_user_tag")
def twitter_publish_user(sender, instance, **kwargs):
    try:
        twitter.update_status(status='Congratulations ' + instance.username + ' for registering on BloodLineDonation, your help is very much appreciated!!!')
    except Exception as e:
        print("ERROR (TWITTER POST): " + str(e))

@receiver(post_save, sender=BloodlineBank, dispatch_uid="twitter_publish_bank_tag")
def twitter_publish_bank(sender, instance, **kwargs):
    try:
        twitter.update_status(status='Welcome aboard ' + instance.name + ', thank you for supporting BloodLineDonation by being a blood bank!!!')
    except Exception as e:
        print("ERROR (TWITTER POST): " + str(e))

@receiver(post_save, sender=BloodlineBlood, dispatch_uid="twitter_publish_blood_tag")
def twitter_publish_blood(sender, instance, **kwargs):
    try:
        twitter.update_status(status=instance.user.username + ' is just being awesome by donating their blood on BloodLineDonation on ' + instance.bank.name + ' bank!!! (' + instance.donor_date.strftime('%d-%m-%Y') + ')')
    except Exception as e:
        print("ERROR (TWITTER POST): " + str(e))


"""views.py

This module handles most of common view or requests from client

Variables:
	User {models} -- This variable provided the user model from the database to be used for User activation
	blood_type_dict {dictionary} -- this dictionary is used fo dynamic blood type search with ajax
"""

import json

from django.contrib.admin.views.decorators import user_passes_test
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_text
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.decorators.csrf import csrf_exempt
from django.views import generic

from .models import BloodlineUser, BloodlineBank, BloodlineBlood, BLOOD_CHOICES
from .tokens import account_activation_token
from .forms import BloodlineUserForm

User = get_user_model()
blood_type_dict = dict(BLOOD_CHOICES)

# Main page of the staff/administrator control
@user_passes_test(lambda u: u.is_staff)
def staff_main(request):
    return render(request, 'bloodline/staff_main.html')

# Page to provide user registration
def signup(request):
    if request.method == 'POST':
        form = BloodlineUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            # Set/make sure the user activation to false to provide email confirmation to verify it later
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('bloodline/registration/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })

            # get raw password from user input, first row of the password field
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            mail_subject = 'Activate your BloodLine account.'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        # Assign provided user form for user registration on the presentation layer
        form = BloodlineUserForm()
    return render(request, 'bloodline/registration/signup.html', {'form': form})

# Class of index/main/home page
class Home(generic.ListView):
	# Uses the html template to contain the data required
    template_name = 'bloodline/home.html'

    # Give a 'tag' for dataset to be provided to the presentation layer
    context_object_name = 'donor_list'

    def get_queryset(self):
        # If user is aunthenticated, show the 10 recent donation that they making/made
        if self.request.user.is_authenticated():
            return BloodlineBlood.objects.filter(user=self.request.user).order_by('-donor_date')[:10]

# Used as the header of most pages for BloodLine
def header(request):
    return render(request, 'bloodline/header.html')

# Used as the 'form' for ajax search UI
def base_search(request):
    return render(request, 'bloodline/base_search.html')

# Used to let user to plan the blood donation or the staff
def appointment(request):
    return render(request, 'bloodline/appointment_request.html')

# Provide the service for user email confirmation function8
def activate(request, uidb64, token, backend='django.contrib.auth.backends.ModelBackend'):
    try:
        # Get the text version or safe url in base64 form
        uid = force_text(urlsafe_base64_decode(uidb64))

        # Get user object based on the user that just registered
        user = User.objects.get(pk=uid)

    # If there's TypeError, ValueError, OverflowError, or user is not exist, set the user to 'none' or 'nothing'
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    # If user and account activation token is valid then set the user as 'confirmed' then log user in
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        # If user is none or account activation token is invalied then return 'Activation link is invalid!'
        return HttpResponse('Activation link is invalid!')

# AJAX function to search blood bank centre by address and postcode
@csrf_exempt
def list_centre(request):
	# Get the key_words from ajax
    key_words = request.POST.get('key_words')
    rejson = []

    # Select blood bank object based on postcode or address containing the key_words
    recontents_postcode = BloodlineBank.objects.filter(postcode__icontains=key_words)
    recontents_address = BloodlineBank.objects.filter(address__icontains=key_words)

    # Appending selected data into rejson list
    for recontent_postcode in recontents_postcode:

        # Put in blood bank name, address, postcode, phone and email into the list to return to user
        rejson.append(
            "BLOOD BANK CENTER: " + str(recontent_postcode.name) + " | " + str(recontent_postcode.address) + ", " + str(
                recontent_postcode.postcode) + " | " + str(recontent_postcode.phone) + " | " + str(
                recontent_postcode.email))
    for recontent_address in recontents_address:
        rejson.append(
            "BLOOD BANK CENTER: " + str(recontent_address.name) + " | " + str(recontent_address.address) + ", " + str(
                recontent_address.postcode) + " | " + str(recontent_address.phone) + " | " + str(
                recontent_address.email))

    # Sort the data inside rejson list
    rejson.sort()

    # Make the list 'unique', throw away the duplicates
    rejson = list(set(rejson))

    # Return the rejson data into the UI via AJAX
    return HttpResponse(json.dumps(rejson), content_type='application/json')

# AJAX function to search public profile that has specific blood type
@csrf_exempt
def list_blood(request):
	# Get the key_words from ajax
    key_words = request.POST.get('key_words')
    rejson = []

    # set the current type to keep track of which blood type that user are looking for
    current_type = 0

    # For every item in blood type list, if there's containg what's in the key_words, then put the 'code' into the current_type
    for each_type in blood_type_dict:
        if key_words.lower() in blood_type_dict[each_type].lower():
            current_type = each_type

    # If current type doesn't change, that means the blood type that user are searching for is not available on public
    if current_type == 0:
        return HttpResponse(json.dumps([]), content_type='application/json')

    # Select user object based on what blood type code that's being searched
    recontents = BloodlineUser.objects.filter(blood_type=current_type, public_profile=True)
    for recontent in recontents:

        # Put in user's username, blood type, address, mobile, and email into the list to return to user
        rejson.append("USER: " + str(recontent.username) + " | " + str(recontent.get_blood_type()) + " | " + str(
            recontent.address) + " | " + str(recontent.mobile) + " | " + str(recontent.email))

    # Sort the data inside rejson list
    rejson.sort()

    # Make the list 'unique', throw away the duplicates
    rejson = list(set(rejson))

    # Return the rejson data into the UI via AJAX
    return HttpResponse(json.dumps(rejson), content_type='application/json')

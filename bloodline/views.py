import json

from django.contrib.admin.views.decorators import user_passes_test
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
# from django.shortcuts import redirect
from django.shortcuts import render
# from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.encoding import force_text
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
# from django.views import generic
from django.views.decorators.csrf import csrf_exempt
# from django.views.generic.edit import View
from django.views import generic

# from .forms import SignUpForm
from .models import BloodlineUser, BloodlineBank, BloodlineBlood, BLOOD_CHOICES  # , BloodlineAppointment
from .tokens import account_activation_token
# from .forms import SignUpForm, ForgetPwdForm, ModifyPwdForm
from .forms import BloodlineUserForm

User = get_user_model()
blood_type_dict = dict(BLOOD_CHOICES)


@user_passes_test(lambda u: u.is_staff)
def staff_main(request):
    return render(request, 'bloodline/staff_main.html')


def signup(request):
    if request.method == 'POST':
        form = BloodlineUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('bloodline/registration/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            mail_subject = 'Activate your BloodLine account.'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = BloodlineUserForm()
    return render(request, 'bloodline/registration/signup.html', {'form': form})


# def home(request):
#     return render(request, 'bloodline/home.html')
# @login_required
class Home(generic.ListView):
    template_name = 'bloodline/home.html'
    context_object_name = 'donor_list'

    def get_queryset(self):
        if self.request.user.is_authenticated():
            return BloodlineBlood.objects.filter(user=self.request.user).order_by('-donor_date')[:10]
        # return BloodlineBlood.objects.filter(user=self.request.user)[:10]


def header(request):
    return render(request, 'bloodline/header.html')


def base_search(request):
    return render(request, 'bloodline/base_search.html')


@login_required
def appointment(request):
    return render(request, 'bloodline/appointment_request.html')


def activate(request, uidb64, token, backend='django.contrib.auth.backends.ModelBackend'):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


@csrf_exempt
def list_centre(request):
    key_words = request.POST.get('key_words')
    rejson = []
    recontents_postcode = BloodlineBank.objects.filter(postcode__icontains=key_words)
    recontents_address = BloodlineBank.objects.filter(address__icontains=key_words)
    for recontent_postcode in recontents_postcode:
        rejson.append(
            "BLOOD BANK CENTER: " + str(recontent_postcode.name) + " | " + str(recontent_postcode.address) + ", " + str(
                recontent_postcode.postcode) + " | " + str(recontent_postcode.phone) + " | " + str(
                recontent_postcode.email))
    for recontent_address in recontents_address:
        rejson.append(
            "BLOOD BANK CENTER: " + str(recontent_address.name) + " | " + str(recontent_address.address) + ", " + str(
                recontent_address.postcode) + " | " + str(recontent_address.phone) + " | " + str(
                recontent_address.email))
    rejson.sort()
    rejson = list(set(rejson))
    return HttpResponse(json.dumps(rejson), content_type='application/json')


@csrf_exempt
def list_blood(request):
    key_words = request.POST.get('key_words')
    rejson = []
    current_type = 0
    for each_type in blood_type_dict:
        if key_words.lower() in blood_type_dict[each_type].lower():
            current_type = each_type
    print(blood_type_dict[current_type].lower())
    if current_type == 0:
        return HttpResponse(json.dumps([]), content_type='application/json')
    recontents = BloodlineUser.objects.filter(blood_type=current_type, public_profile=True)
    for recontent in recontents:
        rejson.append("USER: " + str(recontent.username) + " | " + str(recontent.get_blood_type()) + " | " + str(
            recontent.address) + " | " + str(recontent.mobile) + " | " + str(recontent.email))
    rejson.sort()
    rejson = list(set(rejson))
    return HttpResponse(json.dumps(rejson), content_type='application/json')

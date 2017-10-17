import json

from django.contrib.admin.views.decorators import user_passes_test
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
# from django.contrib.sites.shortcuts import get_current_site
# from django.core.mail import EmailMessage
from django.http import HttpResponse
# from django.shortcuts import redirect
from django.shortcuts import render
# from django.template import RequestContext
from django.template.loader import render_to_string
# from django.utils.encoding import force_text
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
# from django.views import generic
from django.views.decorators.csrf import csrf_exempt
# from django.views.generic.edit import View

# from .forms import SignUpForm
# from .models import BloodlineUser, BloodlineBank
from .tokens import account_activation_token
# from .forms import SignUpForm, ForgetPwdForm, ModifyPwdForm
from .forms import BloodlineUserForm


User = get_user_model()


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
            message = render_to_string('bloodline/templates/registration/acc_active_email.html', {
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
            # login(request, user)
            # return redirect('bloodline_app:home')
    else:
        form = BloodlineUserForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def home(request):
    return render(request, 'bloodline/home.html')


def header(request):
    return render(request, 'bloodline/header.html')


def test(request):
    return render(request, 'bloodline/test.html')


def base_search(request):
    return render(request, 'bloodline/base_search.html')

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
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

@csrf_exempt
# TODO: might not safe here
def list_centre(request):
    key_words = request.POST.get('key_words')
    print(key_words)
    recontents = BloodlineBank.objects.filter(postcode=key_words)
    print(recontents)
    rejson = []
    for recontent in recontents:
        rejson.append(recontent.name)
    return HttpResponse(json.dumps(rejson), content_type='application/json')

# TODO: this is social authentication sample page, merge with main login
def social_auth(request):
    return render(request, 'bloodline/social_auth.html')

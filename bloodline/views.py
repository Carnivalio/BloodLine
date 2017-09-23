from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.views.generic.edit import View
from django.contrib.auth.hashers import make_password

from .forms import SignUpForm
from .models import BloodlineUser
from .tokens import account_activation_token
from .forms import SignUpForm, ForgetPwdForm, ModifyPwdForm


User = get_user_model()


class IndexView(generic.ListView):
    template_name = 'bloodline/index.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        return BloodlineUser.objects.all().order_by('-pk')[:10]


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            #            user.refresh_from_db()  # load the profile instance created by the signal
            # user.profile.birth_date = form.cleaned_data.get('birth_date')
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
        form = SignUpForm()
    return render(request, 'bloodline/signup.html', {'form': form})


@login_required
def home(request):
    return render(request, 'bloodline/home.html')


def header(request):
    return render(request, 'bloodline/header.html')


def test(request):
    return render(request, 'bloodline/test.html')


def base_search(request):
    return render(request, 'bloodline/base_search.html')


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





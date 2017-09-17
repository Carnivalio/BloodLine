from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from .models import BloodlineUser, BloodlineBank, BloodlineBlood
from .forms import BloodlineUserForm, BloodlineBankForm, BloodlineBloodForm, SignUpForm

class IndexView(generic.ListView):
    template_name = 'bloodline/index.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        return BloodlineUser.objects.all().order_by('-pk')[:10]

@login_required
def home(request):
    return render(request, 'bloodline/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('bloodline_app:home')
    else:
        form = SignUpForm()
    return render(request, 'bloodline/signup.html', {'form': form})

@login_required
def home(request):
    return render(request, 'core/home.html')
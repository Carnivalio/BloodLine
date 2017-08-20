from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import redirect

from .models import User, Bank, Blood
from .forms import UserForm, BankForm, BloodForm

class IndexView(generic.ListView):
    template_name = 'bloodline/index.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        return User.objects.all().order_by('-id')[:20]

class DetailView(generic.DetailView):
    model = User
    template_name = 'bloodline/detail.html'

def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/bloodline')
    else:
        form = UserForm()
    return render(request, "bloodline/add_user.html", {'form': form})
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.utils import timezone
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from .models import User, Bank, Blood
from .forms import UserForm, BankForm, BloodForm

class IndexView(generic.ListView):
    template_name = 'bloodline/index.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        return User.objects.all().order_by('-id')[:10]

class DetailView(generic.DetailView):
    model = User
    template_name = 'bloodline/user_detail.html'

class CreateUser(SuccessMessageMixin, CreateView):
    template_name = 'bloodline/user_create.html'
    success_url = reverse_lazy('bloodline_app:index')
    model = User
    fields = ['email', 'username', 'password', 'first_name', 'last_name', 'mobile', 'address', 'blood_type', 'verified']
    template_name_suffix = '_create_form'
    success_message = "User successfully created!"

class UpdateUser(UpdateView):
    template_name = 'bloodline/user_update.html'
    model = User
    success_url = reverse_lazy('bloodline_app:index')
    fields = ['email', 'username', 'password', 'first_name', 'last_name', 'mobile', 'address', 'blood_type', 'verified']
    template_name_suffix = '_update_form'

class DeleteUser(DeleteView):
    template_name = 'bloodline/user_delete.html'
    model = User
    success_url = reverse_lazy('bloodline_app:index')
    template_name_suffix = '_confirm_delete'
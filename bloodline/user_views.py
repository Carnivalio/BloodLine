from django.contrib.admin.views.decorators import user_passes_test
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import BloodlineUserForm
from .models import BloodlineUser

class UserListView(generic.ListView):
    template_name = 'bloodline/user_template/user_list.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        return BloodlineUser.objects.all().order_by('-pk')[:100]

class DetailUser(generic.DetailView):
    model = BloodlineUser
    context_object_name = 'bloodlineuser'
    template_name = 'bloodline/user_template/user_detail.html'

class CreateUser(CreateView):
    template_name = 'bloodline/user_template/user_create.html'
    success_url = reverse_lazy('bloodline_app:user_list')
    model = BloodlineUser
    form_class = BloodlineUserForm
    template_name_suffix = '_create_form'

class UpdateUser(UpdateView):
    template_name = 'bloodline/user_template/user_update.html'
    model = BloodlineUser
    fields = ['username', 'email', 'password', 'gender', 'first_name', 'last_name', 'mobile', 'address', 'blood_type', 'public_profile', 'verified', 'is_active', 'is_staff']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('bloodline_app:user_detail', kwargs={'pk': self.get_object().pk})

class DeleteUser(DeleteView):
    template_name = 'bloodline/user_template/user_delete.html'
    model = BloodlineUser
    success_url = reverse_lazy('bloodline_app:user_list')
    template_name_suffix = '_confirm_delete'

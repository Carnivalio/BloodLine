from django.contrib.admin.views.decorators import user_passes_test
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView


from .forms import BloodlineUserForm
from .models import BloodlineUser

# @user_passes_test(lambda u: u.is_staff)
class UserListView(generic.ListView):
    template_name = 'bloodline/user_list.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        return BloodlineUser.objects.all().order_by('-pk')[:100]

# @user_passes_test(lambda u: u.is_staff)
class DetailUser(generic.DetailView):
    model = BloodlineUser
    context_object_name = 'bloodlineuser'
    template_name = 'bloodline/user_detail.html'

# @user_passes_test(lambda u: u.is_staff)
class CreateUser(CreateView):
    template_name = 'bloodline/user_create.html'
    success_url = reverse_lazy('bloodline_app:user_list')
    model = BloodlineUser
    # fields = ['email', 'username', 'password', 'first_name', 'last_name', 'mobile', 'address', 'blood_type', 'verified']
    # fields = ['username', 'mobile', 'address', 'blood_type', 'verified']
    # fields = ['email', 'username', 'password', 'gender', 'first_name', 'last_name', 'mobile', 'address', 'blood_type', 'verified', 'is_staff', 'is_active', 'is_superuser']
    # fields = ['email', 'username', 'password', 'password', 'gender', 'first_name', 'last_name', 'mobile', 'address', 'blood_type', 'verified', 'is_staff', 'is_active', 'is_superuser']
    form_class = BloodlineUserForm
    # form_class = SignUpForm
    template_name_suffix = '_create_form'
    # success_message = "User successfully created!"

# @user_passes_test(lambda u: u.is_staff)
class UpdateUser(UpdateView):
    template_name = 'bloodline/user_update.html'
    model = BloodlineUser
    fields = ['email', 'username', 'password', 'gender', 'first_name', 'last_name', 'mobile', 'address', 'blood_type',
              'public_profile', 'verified', 'is_staff', 'is_active', 'is_superuser']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        # return reverse('bloodline_app:user_detail', kwargs={'pk': self.get_object().pk})
        return reverse_lazy('bloodline_app:user_detail', kwargs={'pk': self.get_object().pk})

# @user_passes_test(lambda u: u.is_staff)
class DeleteUser(DeleteView):
    template_name = 'bloodline/user_delete.html'
    model = BloodlineUser
    success_url = reverse_lazy('bloodline_app:user_list')
    template_name_suffix = '_confirm_delete'



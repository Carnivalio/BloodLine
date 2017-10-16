from django.contrib.admin.views.decorators import user_passes_test
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView

from .forms import BloodlineUserForm, BloodlineBankForm
from .models import BloodlineUser, BloodlineBank

# @user_passes_test(lambda u: u.is_staff)
class BankListView(generic.ListView):
    template_name = 'bloodline/bank_list.html'
    context_object_name = 'bank_list'

    def get_queryset(self):
        return BloodlineBank.objects.all().order_by('-pk')[:100]

# @user_passes_test(lambda u: u.is_staff)
class DetailBank(generic.DetailView):
    model = BloodlineBank
    context_object_name = 'bloodlinebank'
    template_name = 'bloodline/bank_detail.html'

# @user_passes_test(lambda u: u.is_staff)
class CreateBank(CreateView):
    template_name = 'bloodline/bank_create.html'
    success_url = reverse_lazy('bloodline_app:bank_list')
    model = BloodlineBank
    # fields = ['email', 'username', 'password', 'first_name', 'last_name', 'mobile', 'address', 'blood_type', 'verified']
    # fields = ['username', 'mobile', 'address', 'blood_type', 'verified']
    # fields = ['email', 'username', 'password', 'gender', 'first_name', 'last_name', 'mobile', 'address', 'blood_type', 'verified', 'is_staff', 'is_active', 'is_superuser']
    # fields = ['email', 'username', 'password', 'password', 'gender', 'first_name', 'last_name', 'mobile', 'address', 'blood_type', 'verified', 'is_staff', 'is_active', 'is_superuser']
    form_class = BloodlineBankForm
    # form_class = SignUpForm
    template_name_suffix = '_create_form'
    # success_message = "User successfully created!"

# @user_passes_test(lambda u: u.is_staff)
class UpdateBank(UpdateView):
    template_name = 'bloodline/bank_update.html'
    model = BloodlineBank
    fields = ['name', 'address', 'phone', 'email', 'postcode']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        # return reverse('bloodline_app:user_detail', kwargs={'pk': self.get_object().pk})
        return reverse_lazy('bloodline_app:bank_detail', kwargs={'pk': self.get_object().pk})

# @user_passes_test(lambda u: u.is_staff)
class DeleteBank(DeleteView):
    template_name = 'bloodline/bank_delete.html'
    model = BloodlineBank
    success_url = reverse_lazy('bloodline_app:bank_list')
    template_name_suffix = '_confirm_delete'


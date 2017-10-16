from django.contrib.admin.views.decorators import user_passes_test
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from datetimewidget.widgets import DateTimeWidget

from .forms import BloodlineUserForm, BloodlineBankForm, BloodlineBloodForm
from .models import BloodlineUser, BloodlineBank, BloodlineBlood

# @user_passes_test(lambda u: u.is_staff)
class BloodListView(generic.ListView):
    # @method_decorator(user_passes_test(lambda u: u.is_staff))
    template_name = 'bloodline/blood_list.html'
    context_object_name = 'blood_list'

    def get_queryset(self):
        return BloodlineBlood.objects.all().order_by('-pk')[:100]

# @user_passes_test(lambda u: u.is_staff)
class DetailBlood(generic.DetailView):
    model = BloodlineBlood
    context_object_name = 'bloodlineblood'
    template_name = 'bloodline/blood_detail.html'

# @user_passes_test(lambda u: u.is_staff)
class CreateBlood(CreateView):
    template_name = 'bloodline/blood_create.html'
    success_url = reverse_lazy('bloodline_app:blood_list')
    model = BloodlineBlood
    # fields = ['email', 'username', 'password', 'first_name', 'last_name', 'mobile', 'address', 'blood_type', 'verified']
    # fields = ['username', 'mobile', 'address', 'blood_type', 'verified']
    # fields = ['email', 'username', 'password', 'gender', 'first_name', 'last_name', 'mobile', 'address', 'blood_type', 'verified', 'is_staff', 'is_active', 'is_superuser']
    # fields = ['email', 'username', 'password', 'password', 'gender', 'first_name', 'last_name', 'mobile', 'address', 'blood_type', 'verified', 'is_staff', 'is_active', 'is_superuser']
    form_class = BloodlineBloodForm
    # form_class = SignUpForm
    template_name_suffix = '_create_form'
    # success_message = "User successfully created!"

# @user_passes_test(lambda u: u.is_staff)
class UpdateBlood(UpdateView):
    template_name = 'bloodline/blood_update.html'
    model = BloodlineBlood
    form_class = BloodlineBloodForm
    # fields = ['user', 'bank', 'donor_date', 'blood_status']
    # widgets = {'donor_date': DateTimeWidget(attrs = {'id':'id_dateTimeField'}, bootstrap_version=3)}
    template_name_suffix = '_update_form'

    def get_success_url(self):
        # return reverse('bloodline_app:user_detail', kwargs={'pk': self.get_object().pk})
        return reverse_lazy('bloodline_app:blood_detail', kwargs={'pk': self.get_object().pk})

# @user_passes_test(lambda u: u.is_staff)
class DeleteBlood(DeleteView):
    template_name = 'bloodline/blood_delete.html'
    model = BloodlineBlood
    success_url = reverse_lazy('bloodline_app:blood_list')
    template_name_suffix = '_confirm_delete'


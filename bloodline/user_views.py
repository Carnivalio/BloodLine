"""user_views.py

This module handle mostly of administrator/staff function related to user
"""

from django.contrib.admin.views.decorators import user_passes_test
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import BloodlineUserForm
from .models import BloodlineUser

# This class provide the list of users on Bloodline (for staff/administrator)
class UserListView(generic.ListView):
	# The template location to be used for this view
    template_name = 'bloodline/user_template/user_list.html'

    # The dataset context name for presentation layer
    context_object_name = 'user_list'

    # This function get all registered users, filter and the the latest 100 of them and then return to presentation layer
    def get_queryset(self):
        return BloodlineUser.objects.all().order_by('-pk')[:100]

# This class provide the detail of user on Bloodline (for staff/administrator)
class DetailUser(generic.DetailView):
	# The model to be used for this view (read models.py)
    model = BloodlineUser
    context_object_name = 'bloodlineuser'
    template_name = 'bloodline/user_template/user_detail.html'

# This class provide the form to create a user on Bloodline (for staff/administrator)
class CreateUser(CreateView):
    template_name = 'bloodline/user_template/user_create.html'

    # After a success of making a user, get back to the routing 'user_list' form bloodline_app
    success_url = reverse_lazy('bloodline_app:user_list')
    model = BloodlineUser
    form_class = BloodlineUserForm
    template_name_suffix = '_create_form'

# This class provide the form to update a user on Bloodline (for staff/administrator)
class UpdateUser(UpdateView):
    template_name = 'bloodline/user_template/user_update.html'
    model = BloodlineUser
    fields = ['username', 'email', 'password', 'gender', 'first_name', 'last_name', 'mobile', 'address', 'blood_type', 'public_profile', 'verified', 'is_active', 'is_staff']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('bloodline_app:user_detail', kwargs={'pk': self.get_object().pk})

# This class provide the form to confirm a user deletion on Bloodline (for staff/administrator)
class DeleteUser(DeleteView):
    template_name = 'bloodline/user_template/user_delete.html'
    model = BloodlineUser
    success_url = reverse_lazy('bloodline_app:user_list')
    template_name_suffix = '_confirm_delete'

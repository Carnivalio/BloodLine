"""bank_views.py

This module handle mostly of administrator/staff function related to blood bank
"""

from django.contrib.admin.views.decorators import user_passes_test
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import BloodlineBankForm
from .models import BloodlineBank

# This class provide the list of blood banks on Bloodline (for staff/administrator)
class BankListView(generic.ListView):
	# The template location to be used for this view
    template_name = 'bloodline/bank_template/bank_list.html'

    # The dataset context name for presentation layer
    context_object_name = 'bank_list'

    # This function get all registered blood banks, filter and the the latest 100 of them and then return to presentation layer
    def get_queryset(self):
        return BloodlineBank.objects.all().order_by('-pk')[:100]

# This class provide the detail of blood bank on Bloodline (for staff/administrator)
class DetailBank(generic.DetailView):
	# The model to be used for this view (read models.py)
    model = BloodlineBank
    context_object_name = 'bloodlinebank'
    template_name = 'bloodline/bank_template/bank_detail.html'

# This class provide the form to create a blood bank on Bloodline (for staff/administrator)
class CreateBank(CreateView):
    template_name = 'bloodline/bank_template/bank_create.html'

    # After a success of making a blood bank, get back to the routing 'bank_list' form bloodline_app
    success_url = reverse_lazy('bloodline_app:bank_list')
    model = BloodlineBank
    form_class = BloodlineBankForm
    template_name_suffix = '_create_form'

# This class provide the form to update a blood bank on Bloodline (for staff/administrator)
class UpdateBank(UpdateView):
    template_name = 'bloodline/bank_template/bank_update.html'
    model = BloodlineBank
    fields = ['name', 'address', 'phone', 'email', 'postcode']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('bloodline_app:bank_detail', kwargs={'pk': self.get_object().pk})

# This class provide the form to confirm a blood bank deletion on Bloodline (for staff/administrator)
class DeleteBank(DeleteView):
    template_name = 'bloodline/bank_template/bank_delete.html'
    model = BloodlineBank
    success_url = reverse_lazy('bloodline_app:bank_list')
    template_name_suffix = '_confirm_delete'

"""blood_views.py

This module handle mostly of administrator/staff function related to blood donation
"""
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required

from .forms import BloodlineBloodForm, BloodlineBloodFormPublic
from .models import BloodlineBlood
from django.contrib.admin.views.decorators import user_passes_test

# This class provide the list of blood donations on Bloodline (for staff/administrator)
class BloodListView(generic.ListView):
	# The template location to be used for this view
    template_name = 'bloodline/blood_template/blood_list.html'

    # The dataset context name for presentation layer
    context_object_name = 'blood_list'

    # This function get all registered blood donations, filter and the the latest 100 of them and then return to presentation layer
    def get_queryset(self):
        return BloodlineBlood.objects.all().order_by('-pk')[:100]

# This class provide the detail of blood donation on Bloodline (for staff/administrator)
class DetailBlood(generic.DetailView):
	# The model to be used for this view (read models.py)
    model = BloodlineBlood
    context_object_name = 'bloodlineblood'
    template_name = 'bloodline/blood_template/blood_detail.html'

# This class provide the form to create a blood donation on Bloodline (for staff/administrator)
class CreateBlood(CreateView):
    template_name = 'bloodline/blood_template/blood_create.html'

    # After a success of making a blood donation, get back to the routing 'blood_list' form bloodline_app
    success_url = reverse_lazy('bloodline_app:blood_list')
    model = BloodlineBlood
    form_class = BloodlineBloodForm
    template_name_suffix = '_create_form'

# This class provide the form to update a blood donation on Bloodline (for staff/administrator)
class CreateBloodPublic(CreateView):
    template_name = 'bloodline/appointment_request.html'
    success_url = reverse_lazy('bloodline_app:home')
    model = BloodlineBlood
    form_class = BloodlineBloodFormPublic
    template_name_suffix = '_create_form'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.blood_status = 0
        obj.save()
        return HttpResponseRedirect(reverse_lazy('bloodline_app:home'))

# This class provide the form to confirm a blood donation deletion on Bloodline (for staff/administrator)
class UpdateBlood(UpdateView):
    template_name = 'bloodline/blood_template/blood_update.html'
    model = BloodlineBlood
    form_class = BloodlineBloodForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('bloodline_app:blood_detail', kwargs={'pk': self.get_object().pk})

class DeleteBlood(DeleteView):
    template_name = 'bloodline/blood_template/blood_delete.html'
    model = BloodlineBlood
    success_url = reverse_lazy('bloodline_app:blood_list')
    template_name_suffix = '_confirm_delete'

from django.urls import reverse_lazy
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required

from .forms import BloodlineBloodForm, BloodlineBloodFormPublic
from .models import BloodlineBlood
from django.contrib.admin.views.decorators import user_passes_test


class BloodListView(generic.ListView):
    template_name = 'bloodline/blood_template/blood_list.html'
    context_object_name = 'blood_list'

    def get_queryset(self):
        return BloodlineBlood.objects.all().order_by('-pk')[:100]

class DetailBlood(generic.DetailView):
    model = BloodlineBlood
    context_object_name = 'bloodlineblood'
    template_name = 'bloodline/blood_template/blood_detail.html'

class CreateBlood(CreateView):
    template_name = 'bloodline/blood_template/blood_create.html'
    success_url = reverse_lazy('bloodline_app:blood_list')
    model = BloodlineBlood
    form_class = BloodlineBloodForm
    template_name_suffix = '_create_form'

@login_required
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

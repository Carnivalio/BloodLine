from django.contrib.admin.views.decorators import user_passes_test
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from datetimewidget.widgets import DateTimeWidget

from .forms import BloodlineBloodForm
from .models import BloodlineBlood

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

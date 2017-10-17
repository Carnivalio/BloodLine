from django.contrib.admin.views.decorators import user_passes_test
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import BloodlineBankForm
from .models import BloodlineBank

class BankListView(generic.ListView):
    template_name = 'bloodline/bank_template/bank_list.html'
    context_object_name = 'bank_list'

    def get_queryset(self):
        return BloodlineBank.objects.all().order_by('-pk')[:100]

class DetailBank(generic.DetailView):
    model = BloodlineBank
    context_object_name = 'bloodlinebank'
    template_name = 'bloodline/bank_template/bank_detail.html'

class CreateBank(CreateView):
    template_name = 'bloodline/bank_template/bank_create.html'
    success_url = reverse_lazy('bloodline_app:bank_list')
    model = BloodlineBank
    form_class = BloodlineBankForm
    template_name_suffix = '_create_form'

class UpdateBank(UpdateView):
    template_name = 'bloodline/bank_template/bank_update.html'
    model = BloodlineBank
    fields = ['name', 'address', 'phone', 'email', 'postcode']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('bloodline_app:bank_detail', kwargs={'pk': self.get_object().pk})

class DeleteBank(DeleteView):
    template_name = 'bloodline/bank_template/bank_delete.html'
    model = BloodlineBank
    success_url = reverse_lazy('bloodline_app:bank_list')
    template_name_suffix = '_confirm_delete'

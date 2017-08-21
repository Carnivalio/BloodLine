from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import redirect

from .models import User, Bank, Blood
from .forms import UserForm, BankForm, BloodForm

"""
This class renders index page, which demonstrates all
the users registered on the website
"""
class IndexView(generic.ListView):
    template_name = 'bloodline/index.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        return User.objects.all().order_by('-id')[:20]

"""
This class renders user details page, which demonstrates
the personal information of a specific user
"""
class DetailView(generic.DetailView):
    model = User
    # Specify the templete using for details page
    template_name = 'bloodline/detail.html'


def add_user(request):
    """
    This function implements adding user to the detail page
    """
    if request.method == "POST":
        # Get data from the posted form
        form = UserForm(request.POST)
        # Validate the posted data (Handled by the model)
        if form.is_valid():
            model_instance = form.save(commit=False) # Save the user input data into the form object
            model_instance.timestamp = timezone.now() # Get the current timestamp for the logging purpose
            model_instance.save() # Save the data from the form into the database through model
            return redirect('/bloodline') # Redirect to the index page
    else:
        form = UserForm()
    return render(request, "bloodline/add_user.html", {'form': form})
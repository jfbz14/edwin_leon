from django.shortcuts import render,redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.conf import settings

# model
from .forms import FormUserProfile

# Create your views here.


class FormUserView(FormView):
    """ create supplie """

    template_name = 'form/form_user.html'
    form_class = FormUserProfile
    print (settings.DEBUG)

    def form_valid(self, form):
        """Save form data."""
        
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        url = "%s?register=register_valid" % reverse('forms_users:register')
        return url
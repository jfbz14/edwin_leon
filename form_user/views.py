from django.urls import reverse
from django.views.generic import FormView

# model
from .forms import FormUserProfile
from .models import CommuneModel, NeighborhoodModel

# Create your views here.

class FormUserView(FormView):
    """ create supplie """

    template_name = 'form/form_user.html'
    form_class = FormUserProfile
    extra_context = {
        'communes': CommuneModel.objects.all().order_by('id'),
        'neighborhoods' : NeighborhoodModel.objects.all().order_by('name_neighborhood'),
        }

    def form_valid(self, form):
        """Save form data."""
        
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        url = "%s?register=register_valid" % reverse('forms_users:register')
        return url
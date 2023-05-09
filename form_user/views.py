from django.urls import reverse
from django.views.generic import FormView, TemplateView

# model
from .forms import FormUserProfile, FormUserLeader
from .models import CommuneModel, NeighborhoodModel

# Create your views here.

class CreateFormUserProfileView(FormView):
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


class CreateFormUserLeaderView(FormView):
    """ create supplie """

    template_name = 'form/form_leader.html'
    form_class = FormUserLeader

    def form_valid(self, form):
        """Save form data."""
        
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        url = "%s?register=register_valid" % reverse('forms_users:register_leader')
        return url
    
    
class TemplateHome(TemplateView):
    
    template_name = "page/home.html"
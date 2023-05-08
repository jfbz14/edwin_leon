# Django
from django import forms
from datetime import datetime, timedelta
from django_select2 import forms as s2forms

#model
from .models import UserProfile, UserLeader


class AuthorWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "first_name__icontains",
        "last_name__icontains",
    ]
    empty_label= 'Seleccione lider'

    def build_attrs(self, base_attrs, extra_attrs=None):
        return super().build_attrs(base_attrs, extra_attrs={'class':'w-full '})


class FormUserProfile(forms.ModelForm):
    """model form"""

    class Meta:
        """Form settings"""

        model = UserProfile
        exclude = ['is_valid']
        widgets = {
            "leader": AuthorWidget,
        }

    def clean_date(self):
        """ validate date valid. """

        date = self.cleaned_data['date']
        date_today = datetime.now().date()
        min_days = timedelta(days=6570).days
        date_valid = (date_today - date).days  
        
        if date > date_today:
            raise forms.ValidationError('Fecha no futura')
        elif min_days > date_valid:
            raise forms.ValidationError('Fecha invalida')          
        else:
            return date
    
    def clean_commune(self):
        """ validate field. """

        commune = self.cleaned_data['commune']

        if commune.upper() == '' or commune == 'COMUNA*':
            raise forms.ValidationError('Seleccionar comuna')
        return commune

    def clean_neighborhood(self):
        """ validate field. """

        neighborhood = self.cleaned_data['neighborhood']

        if neighborhood.upper() == '' or neighborhood == 'BARRIO*':
            raise forms.ValidationError('Seleccionar barrio')
        return neighborhood


class FormUserLeader(forms.ModelForm):
    """model form"""

    class Meta:
        """Form settings"""

        model = UserLeader
        fields = "__all__"

    def clean_date(self):
        """ validate date valid. """

        date = self.cleaned_data['date']
        date_today = datetime.now().date()
        min_days = timedelta(days=6570).days
        date_valid = (date_today - date).days  
        
        if date > date_today:
            raise forms.ValidationError('Fecha no futura')
        elif min_days > date_valid:
            raise forms.ValidationError('Fecha invalida')          
        else:
            return date


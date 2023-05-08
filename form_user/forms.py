# Django
from django import forms
from datetime import datetime, timedelta

#model
from .models import UserProfile, UserLeader


class FormUserProfile(forms.ModelForm):
    """model form"""

    class Meta:
        """Form settings"""

        model = UserProfile
        exclude = ['is_valid']

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

        if commune == '' or commune == 'Comuna*':
            raise forms.ValidationError('Seleccionar comuna')
        return commune

    def clean_neighborhood(self):
        """ validate field. """

        neighborhood = self.cleaned_data['neighborhood']

        if neighborhood == '' or neighborhood == 'Barrio*':
            raise forms.ValidationError('Seleccionar barrio')
        return neighborhood


class FormUserProfile(forms.ModelForm):
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


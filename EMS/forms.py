from django import forms 
from .models import Event,Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=Registration
        fields=['full_name','email','ph_no']

from django import forms
from . models import Contacto

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['name', 'email', 'message']

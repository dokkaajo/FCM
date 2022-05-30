from django import forms
from django.forms.models import ModelForm
from projet.models import citoyen

class CitoyenForm(forms.Form,ModelForm):
    class Meta:
        model=citoyen
        fields=['c_UserID','c_Residence','c_Nationalite','c_Image']
        widgets = {'c_UserID': forms.HiddenInput() }


from django import forms
from django.forms.models import ModelForm
from  projet.models import  CvCitoyen

class AddCvForm(forms.Form,ModelForm):
    class Meta:
        model=CvCitoyen
        fields=['cvCitoyenID','cvTitre','cvNiveauEtude','cvGrade','cvResume','cvCitoyenPdf']
        widgets = {'cvCitoyenID': forms.HiddenInput()}

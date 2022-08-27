from random import choices
from django import forms
from django.forms import ModelForm
from .models import Destination, Next


class DestinationForm(ModelForm):
    class Meta:
        model = Destination
        fields = ('city', 'country', 'adventure', 'climate', 'flight', 'image')
        labels = {
            'city': 'City',
            'country': 'Country',
            'adventure': 'Type of Adventure',
            'climate': 'Climate',
            'flight': 'Flight Time',
            'image': 'Image',
        }
        widgets = {
            'City': forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}),
            'Country': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country'}),
            'Adventure': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Adventure'}),
            'Climate': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Climate'}),
            'Flight': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Flight'}),
            'Image': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Image'}),
        }

class NextDestination(ModelForm):

    class Meta:   
        model = Next
        fields = "__all__"

        widgets = {
            'adventure': forms.Select(attrs={'class':'form-select'}),
            'climate': forms.Select(attrs={'class':'form-select'}),
            'flight': forms.Select(attrs={'class':'form-select'}),
        }
from .models import *
from django import forms


class DNSForm(forms.ModelForm):
    
    class Meta:
        model =  DNS
        fields = '__all__'
        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'ip': forms.TextInput(attrs={'class': 'form-control'}),
                'tipo': forms.Select(attrs={'class': 'form-select'}),
        }
    

class DNSEntryForm(forms.ModelForm):
    class Meta:
        model =  DNSEntry
        fields = '__all__'
        widgets = {
                'entry_name': forms.TextInput(attrs={'class': 'form-control'}),
                'entry_type': forms.Select(attrs={'class': 'form-control'}),
                'value': forms.TextInput(attrs={'class': 'form-control'}),
                'server': forms.Select(attrs={'class': 'form-select'}),
                'dns_server': forms.Select(attrs={'class': 'form-select'}),
                'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            }
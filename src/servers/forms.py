from .models import OS, Server

from django import forms


#Formularios que sera utilziaedo para crear los OS
class OSForm(forms.ModelForm):
    class Meta:
        model = OS
        #Campos que vamos a mostrar del form
        fields = ['nombre', 'version','os_img', 'os_type']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'version': forms.TextInput(attrs={'class': 'form-control'}),
            'os_type': forms.Select(attrs={'class': 'form-select'}),
            'os_img': forms.ClearableFileInput(attrs={'class': 'form-control'}),

        }
        
class ServerForm(forms.ModelForm):
    class Meta:
        model = Server
        #Campos que vamos a mostrar del form
        fields = '__all__'
        widgets = {
            'server_name': forms.TextInput(attrs={'class': 'form-control'}),
            'ip': forms.TextInput(attrs={'class': 'form-control'}),
            'server_hostname': forms.TextInput(attrs={'class': 'form-control'}),
            'server_os': forms.Select(attrs={'class': 'form-select'}),
            'server_environment': forms.Select(attrs={'class': 'form-select'}),
            'server_status': forms.Select(attrs={'class': 'form-select'}),
        }
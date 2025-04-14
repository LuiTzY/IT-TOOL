from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Introduce tu contraseña',
            'minlength':'4'
        }
    ))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
         attrs={
            'class':'form-control',
            'placeholder':'Confirme su contraseña',
            'minlength':'4'
        }
    ))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']  
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Introduzca su nombre',
                    'minlength':'4'
                    
                    }
                ),
            'last_name': forms.TextInput(
                attrs={
                'class':'form-control',
                'placeholder':'Introduzca sus apellidos',
                'minlength':'4'
                }
                                         ),
            'username': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Introduzca su correo electronico'
                    }
                )
        }
        
    
    def clean_password2(self):
        # Validación para asegurarse de que las contraseñas coincidan
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if  password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password1

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class AunthenticaUser(forms.ModelForm):


    class Meta:
        model = User
        fields = ("username","password")
        widgets = {
            'username': forms.TextInput(attrs={
                'class':'form-control mt-3',
                'placeholder':'Introduce tu correo'
            }),
            'password':forms.PasswordInput(attrs={
                'class':'form-control mt-3',
                'placeholder':"Introduce tu contraseña"
            })
        }

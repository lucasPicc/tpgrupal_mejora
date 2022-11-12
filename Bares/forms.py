from django import forms
from .models import Bares
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

"""
class Bar_formulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField()
    telefono = forms.IntegerField()
"""

class Bar_formulario(forms.ModelForm):
    class Meta: #Indico a que modelo esta vinculado
        model = Bares #Tengo que importar de models.py
        fields = ('__all__') #Campos del modelo que quiero que se muestren aqui
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'placeholder' : 'Ingrese su nombre...',
                    'class' : 'input-curso-name'
                }
            )
        }

class Restaurante_formulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField()
    telefono = forms.IntegerField()

class Heladeria_formulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField()
    telefono = forms.IntegerField()

class Buscar_formulario(forms.Form):
    nombre = forms.CharField(max_length=50)

# CREACION DE FORMULARIO DE EDICION VINCULADO A UN MODELO

class UserEditForm(UserChangeForm):
    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )
    password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña",widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
    
    def clean_password2(self):
        password2 = self.cleaned_data['password2']
        if password2 != self.cleaned_data['password1']:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2
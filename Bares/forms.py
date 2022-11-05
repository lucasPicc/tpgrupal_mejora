from django import forms

class Bar_formulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField()
    telefono = forms.IntegerField()

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
   
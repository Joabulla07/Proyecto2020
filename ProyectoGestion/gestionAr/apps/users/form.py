from django import forms


class Registro(forms.Form):
    dni = forms.IntegerField()
    nombres = forms.CharField()
    apellido = forms.CharField()
    domicilio = forms.CharField()
    mail = forms.EmailField()
    telefono = forms.CharField()


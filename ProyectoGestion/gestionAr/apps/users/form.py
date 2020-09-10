from django import forms
from .models import *

doctor = [
        ('MARIA GOMEZ', 'Dra. MARIA GOMEZ'),
        ('JOANNA BULLA', 'Dra. JOANNA BULLA'),
]


class Registro(forms.Form):
    medicos = forms.ChoiceField(choices=doctor)
    dni = forms.IntegerField()
    nombres = forms.CharField()
    apellido = forms.CharField()
    domicilio = forms.CharField()
    mail = forms.EmailField()
    telefono = forms.CharField()


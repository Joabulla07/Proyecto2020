from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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


class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ('nombres_y_apellido','domicilio','mail', 'telefono')


class UserCreateForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class TurnosMedicoForm(forms.ModelForm):
    class Meta:
        model = TurnosMedico
        fields = ('__all__')
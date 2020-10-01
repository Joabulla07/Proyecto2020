from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Medico(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name="medico")
    nombres_y_apellido = models.CharField(max_length=100)
    domicilio = models.CharField(max_length=100)
    mail = models.EmailField(null=True)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombres_y_apellido

class TurnosMedico(models.Model):
    medico = models.ForeignKey(Medico, on_delete = models.CASCADE, related_name='turnos')
    dni = models.IntegerField(primary_key=True, null=False)
    nombres = models.CharField(max_length=10, null=True)
    apellido = models.CharField(max_length=10, null=True)
    domicilio = models.CharField(max_length=15, null=True)
    mail = models.EmailField(null=True)
    telefono = models.CharField(max_length=15, null=True)
    fecha = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)

    def __str__(self):
        return 'Turno {}'.format(self.apellido)


class ListaTurnosMedico1(models.Model):
    medicos = models.CharField(max_length=15, null=True)
    dni = models.IntegerField(primary_key=True, null=False)
    nombres = models.CharField(max_length=10, null=True)
    apellido = models.CharField(max_length=10, null=True)
    domicilio = models.CharField(max_length=15, null=True)
    mail = models.EmailField(null=True)
    telefono = models.CharField(max_length=15, null=True)
    fecha = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)

    def __str__(self):
        return 'Turno ' + apellido

class ListaTurnosMedico2(models.Model):
    medicos = models.CharField(max_length=15, null=True)
    dni = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=10, null=True)
    apellido = models.CharField(max_length=10, null=True)
    domicilio = models.CharField(max_length=15, null=True)
    mail = models.EmailField(null=True)
    telefono = models.CharField(max_length=15, null=True)
    fecha = models.DateField(null=True)
    hora = models.TimeField(null=True)

    def __str__(self):
        return 'Turno ' + apellido

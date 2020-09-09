from django.db import models
from django.utils import timezone
from model_utils import Choices
# Create your models here.


class Medico(models.Model):
    usuario = models.CharField(primary_key=True,max_length=10, default='MEDICO')
    nombres_y_apellido = models.CharField(max_length=30, default='MARIA GOMEZ')
    domicilio = models.CharField(max_length=15, default='JOSE HERNANDEZ 25')
    mail = models.EmailField(null=True, default='MARIA@GMAILC.COM')
    telefono = models.CharField(max_length=15, default='3624227225')
    password = models.CharField(max_length=15, default='MEDICO')


class Paciente(models.Model):
    medicos = models.CharField(max_length=15, null=True)
    dni = models.IntegerField(primary_key=True, null=False)
    nombres = models.CharField(max_length=10, null=True)
    apellido = models.CharField(max_length=10, null=True)
    domicilio = models.CharField(max_length=15, null=True)
    mail = models.EmailField(null=True)
    telefono = models.CharField(max_length=15, null=True)


class Turno(models.Model): #para poner en el calendario
    hora = models.DateField()
    fecha = models.TimeField()
    dni = models.IntegerField(primary_key=True, null=False)
    nombres = models.CharField(max_length=10, null=True)
    apellido = models.CharField(max_length=10, null=True)
    domicilio = models.CharField(max_length=15, null=True)
    mail = models.EmailField(null=True)
    telefono = models.CharField(max_length=15, null=True)

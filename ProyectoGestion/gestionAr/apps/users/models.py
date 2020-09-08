from django.db import models
from django.utils import timezone
# Create your models here.


class Paciente(models.Model):
    dni = models.IntegerField(primary_key=True, null=False)
    nombres = models.CharField(max_length=10, null=True)
    apellido = models.CharField(max_length=10, null=True)
    domicilio = models.CharField(max_length=15, null=True)
    mail = models.EmailField(null=True)
    telefono = models.CharField(max_length=15, null=True)


class Medico(models.Model):
    usuario = models.CharField(primary_key=True, max_length=10, default='MEDICO')
    nombres = models.CharField(max_length=10, default='MARIA')
    apellido = models.CharField(max_length=10, default='GONZALEZ')
    domicilio = models.CharField(max_length=15, default='JOSE HERNANDEZ 25')
    mail = models.EmailField(null=True, default='MARIA@GMAILC.COM')
    telefono = models.CharField(max_length=15, default='3624227225')
    password = models.CharField(max_length=15, default='MEDICO')


class Turno(models.Model): #para poner en el calendario
    hora = models.DateField()
    fecha = models.TimeField()
    dni = models.IntegerField(primary_key=True, null=False)
    nombres = models.CharField(max_length=10, null=True)
    apellido = models.CharField(max_length=10, null=True)
    domicilio = models.CharField(max_length=15, null=True)
    mail = models.EmailField(null=True)
    telefono = models.CharField(max_length=15, null=True)

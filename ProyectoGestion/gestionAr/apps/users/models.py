from django.db import models
from django.utils import timezone
# Create your models here.

class Consultorio(models.Model):
    cuit = models.IntegerField(primary_key=True, blank=False, null=False)
    password = models.CharField(max_length= 20, default='00', null=False)
    nombreConsultorio = models.CharField(verbose_name='Nombre del consultorio', max_length=10, blank=True, null=False)
    provincia = models.CharField(max_length=15, blank=False, null=False)
    ciudad = models.CharField(max_length=15, blank=False, null=False)
    domicilio = models.TextField(blank=False, null=False)
    mail = models.EmailField()
    telefono = models.CharField(max_length=15, blank=False, null= False)


class Medicos(models.Model):
    dni = models.IntegerField(primary_key=True, blank=False, null=False)
    nombres = models.CharField(max_length=10, blank=False, null=False)
    apellido = models.CharField(max_length=10, blank=False, null=False)
    provincia = models.CharField(max_length=15, blank=False, null=False)
    ciudad = models.CharField(max_length=15, blank=False, null=False)
    mail = models.EmailField()
    telefono = models.CharField(max_length=15, blank=False, null= False)
    especialidad = models.TextField(max_length=20, null=False)
    consultorio = models.OneToOneField('Consultorio', on_delete=models.CASCADE, related_query_name='cuit+')


class Paciente(models.Model):
    dni = models.IntegerField(primary_key=True, null=False)
    nombres = models.CharField(max_length=10, null=True)
    apellido = models.CharField(max_length=10, null=True)
    provincia = models.CharField(max_length=15, null=True)
    ciudad = models.CharField(max_length=15, null=True)
    domicilio = models.CharField(max_length=15, null=True)
    mail = models.EmailField(null=True)
    telefono = models.CharField(max_length=15, null=True)
    password = models.CharField(default=0,max_length=15, null=False)





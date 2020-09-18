from django.db import models

# Create your models here.


class Medico(models.Model):
    usuario = models.CharField(primary_key=True,max_length=10, default='MEDICO')
    nombres_y_apellido = models.CharField(max_length=30, default='MARIA GOMEZ')
    domicilio = models.CharField(max_length=15, default='JOSE HERNANDEZ 25')
    mail = models.EmailField(null=True, default='MARIA@GMAILC.COM')
    telefono = models.CharField(max_length=15, default='3624227225')
    password = models.CharField(max_length=15, default='MEDICO')

    def save(self, *args, **kwargs):
        self.usuario = self.usuario.upper()
        self.nombres_y_apellido = self.nombres_y_apellido.upper()
        self.domicilio = self.domicilio.upper()
        return super(Medico, self).save(*args, **kwargs)


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

    def save(self, *args, **kwargs):
        self.nombres = self.nombres.upper()
        self.apellido = self.apellido.upper()
        self.domicilio = self.domicilio.upper()
        return super(ListaTurnosMedico1, self).save(*args, **kwargs)


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

    def save(self, *args, **kwargs):
        self.nombres = self.nombres.upper()
        self.apellido = self.apellido.upper()
        self.domicilio = self.domicilio.upper()
        return super(ListaTurnosMedico2, self).save(*args, **kwargs)



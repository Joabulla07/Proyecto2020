# Generated by Django 3.1.1 on 2020-09-21 23:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ListaTurnosMedico1',
            fields=[
                ('medicos', models.CharField(max_length=15, null=True)),
                ('dni', models.IntegerField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=10, null=True)),
                ('apellido', models.CharField(max_length=10, null=True)),
                ('domicilio', models.CharField(max_length=15, null=True)),
                ('mail', models.EmailField(max_length=254, null=True)),
                ('telefono', models.CharField(max_length=15, null=True)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('hora', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ListaTurnosMedico2',
            fields=[
                ('medicos', models.CharField(max_length=15, null=True)),
                ('dni', models.IntegerField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=10, null=True)),
                ('apellido', models.CharField(max_length=10, null=True)),
                ('domicilio', models.CharField(max_length=15, null=True)),
                ('mail', models.EmailField(max_length=254, null=True)),
                ('telefono', models.CharField(max_length=15, null=True)),
                ('fecha', models.DateField(null=True)),
                ('hora', models.TimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres_y_apellido', models.CharField(default='MARIA GOMEZ', max_length=30)),
                ('domicilio', models.CharField(default='JOSE HERNANDEZ 25', max_length=15)),
                ('mail', models.EmailField(default='MARIA@GMAILC.COM', max_length=254, null=True)),
                ('telefono', models.CharField(default='3624227225', max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
# Generated by Django 3.1.1 on 2020-09-22 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_turnosmedico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turnosmedico',
            name='medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.medico'),
        ),
    ]

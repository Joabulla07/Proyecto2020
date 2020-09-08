from django.contrib import admin
from ..users.models import Paciente, Medico


admin.site.register(Paciente)
admin.site.register(Medico)





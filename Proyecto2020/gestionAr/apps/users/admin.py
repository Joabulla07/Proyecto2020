from django.contrib import admin

from ..users.models import Medico, ListaTurnosMedico1, ListaTurnosMedico2, TurnosMedico


admin.site.register(Medico)
admin.site.register(ListaTurnosMedico1)
admin.site.register(ListaTurnosMedico2)
admin.site.register(TurnosMedico)

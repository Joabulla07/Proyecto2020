from django.shortcuts import render, redirect
from .form import Registro
from .models import ListaTurnosMedico2, ListaTurnosMedico1
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    form = Registro(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        i = form_data.get("medicos")
        a = form_data.get("dni")
        b = form_data.get("nombres")
        c = form_data.get("apellido")
        f = form_data.get("domicilio")
        g = form_data.get("mail")
        h = form_data.get("telefono")
        if i == "MARIA GOMEZ":
            ListaTurnosMedico1.objects.create(medicos=i, dni=a, nombres=b, apellido=c, domicilio=f, mail=g, telefono=h)
        else:
            ListaTurnosMedico2.objects.create(medicos=i, dni=a, nombres=b, apellido=c, domicilio=f, mail=g, telefono=h)
        return redirect(home)
    return render(request, 'formulario.html', {'form': form})


def usuarioIU(request):
    return render(request, 'base.html')




from django.shortcuts import render, redirect
from .models import Paciente
from .form import Registro
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'index.html')


def login(request):

    return render(request, 'login.html')


def register(request):
    form = Registro(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        a = form_data.get("dni")
        b = form_data.get("nombres")
        c = form_data.get("apellido")
        d = form_data.get("provincia")
        e = form_data.get("ciudad")
        f = form_data.get("domicilio")
        g = form_data.get("mail")
        h = form_data.get("telefono")
        i = form_data.get("password")
        obj = Paciente.objects.create(dni=a, nombres=b, apellido=c, provincia=d, ciudad=e, domicilio=f, mail=g, telefono=h, password=i)
        return redirect(home)
    return render(request, 'formulario.html', {'form': form})


def usuarioIU(request):
    return render(request, 'base.html')


def consultorioIU(request):
    return render(request, 'base.html')



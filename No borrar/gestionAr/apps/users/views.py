from django.shortcuts import render, redirect
from .form import *
from .models import ListaTurnosMedico2, ListaTurnosMedico1
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['user'], password = request.POST['pass'])
        if user is not None:
            auth.login(request, user)
            return redirect(inicioMedico)
        else:
            return render(request, 'login.html', {'error':'Usuario o contraseña inválidos!!'})
    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        userForm = UserCreateForm(request.POST)
        medicoForm = MedicoForm(request.POST)
        if userForm.is_valid() and medicoForm.is_valid():
            if request.POST['password1'] == request.POST['password2']:
                try:
                    user = User.objects.get(username= request.POST['username'])
                    return  render(request, 'register.html', {'error':'Ya existe un usuario con ese nombre.'})
                except User.DoesNotExist:
                    user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                    medico = Medico(user = user, nombres_y_apellido = request.POST['nombres_y_apellido'], domicilio = request.POST['domicilio'], mail = request.POST['mail'], telefono = request.POST['telefono'])
                    medico.save()
                    auth.login(request, user)
                    return redirect(inicioMedico)
            else:
                return render(request, 'register.html', {'error':'Los passwords no coinciden.'})
        else:
            return render(request, 'register.html',{'userForm': userForm, 'medicoForm': MedicoForm})
    else:
        userForm = UserCreateForm()
        medicoForm = MedicoForm()
        return render(request, 'register.html', {'userForm': userForm, 'medicoForm': MedicoForm})

def registrar_turno(request):

    if request.method == 'POST':
        form = TurnosMedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
        else:
            return render(request, 'formulario_turno.html', {'form':form})
    else:
        form = TurnosMedicoForm()
        return render(request, 'formulario_turno.html', {'form':form})


def acceso_incorrecto(request):
    return render(request, 'acceso_incorrecto.html')


def inicioMedico(request):
    if request.user.is_authenticated:
        usuario = request.user
        try:
            medico = usuario.medico
            turnos = request.user.medico.turnos.all()
            return render(request, 'base.html')
        except:
            return redirect(acceso_incorrecto)
    else:
        return redirect(acceso_incorrecto)


def listado_turnos(request):
    return render(request, 'probando_listado.html')


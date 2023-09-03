from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError

# Create your views here.


def home(request):
    # titulo = 'hola mundo'
    return render(request, 'home.html')


def ingresar(request):
    # titulo = 'hola mundo'
    if request.method == 'GET':
        print('ENVIANDO DATOS')
        return render(request, 'ingresar.html', {
            'formularioLogin': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # registrar al usuario
            try:
                user = User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tareas')
            except IntegrityError:
                return render(request, 'ingresar.html', {
                    'formularioLogin': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'ingresar.html', {
            'formularioLogin': UserCreationForm,
            'error': 'Claves Incorrectas'
        })

def tareas(request):
    return render(request,'tareas.html')


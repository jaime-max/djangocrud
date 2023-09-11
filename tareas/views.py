from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import FormularioTareas
from .models import Tareas
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    # titulo = 'hola mundo'
    return render(request, 'home.html')


def registrar(request):
    # titulo = 'hola mundo'
    if request.method == 'GET':
        print('ENVIANDO DATOS')
        return render(request, 'registrarse.html', {
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
                return render(request, 'registrarse.html', {
                    'formularioLogin': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'registrarse.html', {
            'formularioLogin': UserCreationForm,
            'error': 'Claves Incorrectas'
        })

@login_required
def tareas(request):
    listareas = Tareas.objects.filter(
        user=request.user, diacompletado__isnull=True)
    return render(request, 'tareas.html', {
        'lista_tareas': listareas
    })

@login_required
def listareascompletas(request):
    listareas = Tareas.objects.filter(
        user=request.user, diacompletado__isnull=False).order_by('-diacompletado')
    return render(request, 'tareas.html', {
        'lista_tareas': listareas
    })

@login_required
def creartareas(request):
    if request.method == 'GET':
        return render(request, 'crear_tareas.html', {
            'formulario': FormularioTareas
        })
    else:
        try:
            # print(request.POST)
            form = FormularioTareas(request.POST)
            # print(form)
            nueva_tarea = form.save(commit=False)
            nueva_tarea.user = request.user
            nueva_tarea.save()
            return redirect('tareas')
        except ValueError:
            return render(request, 'crear_tareas.html', {
                'formulario': FormularioTareas,
                'error': 'Introdusca datos validos'
            })

@login_required
def detalletareas(request, tarea_id):
    # print(tarea_id)
    if request.method == 'GET':
        tarea = get_object_or_404(Tareas,pk=tarea_id, user = request.user)
        formulario = FormularioTareas(instance=tarea)
        return render(request, 'detalle_tarea.html', {
            'tareas': tarea,
            'formulario': formulario
        })
    else:
        #print(request.POST)
        try:
            tarea = get_object_or_404(Tareas,pk=tarea_id, user = request.user)
            formulario = FormularioTareas(request.POST, instance=tarea)
            formulario.save()
            return redirect('tareas')
        except ValueError:
            return render(request,'detalle_tarea.html',{
                'tareas': tarea,
                'formulario': formulario,
                'error':'Error al actualizar tareas'
            })

@login_required
def tareacompletada(request, tarea_id):
    tarea = get_object_or_404(Tareas, pk= tarea_id, user = request.user)
    if request.method == 'POST':
        tarea.diacompletado = timezone.now()
        tarea.save()
        #redirecciona a la vista de tareas con redirect
        return redirect('tareas')

@login_required
def tareaeliminada(request, tarea_id):
    tarea = get_object_or_404(Tareas, pk= tarea_id, user = request.user)
    if request.method == 'POST':
        tarea.delete()
        #redirecciona a la vista de tareas con redirect
        return redirect('tareas')

@login_required
def cerrarSesion(request):
    logout(request)
    return redirect('home')


def iniciarsesion(request):
    if request.method == 'GET':
        # print(request.POST)
        return render(request, 'iniciar.html', {
            'formulario': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'iniciar.html', {
                'formulario': AuthenticationForm,
                'error': 'El nombre de usuario o contraseña son incorrectos'
            })
        else:
            login(request, user)
            return redirect('tareas')

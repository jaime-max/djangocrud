from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def home(request):
    #titulo = 'hola mundo'
    return render(request,'home.html')

def ingresar(request):
    #titulo = 'hola mundo'
    if request.method == 'GET':
        print('ENVIANDO DATOS')
        return render(request,'ingresar.html',{
            'formularioLogin': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            #registrar al usuario
            try:
                user = User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'])
                user.save()
                return HttpResponse('usuario creado satisfactoriamente')
            except:
                return HttpResponse('Usuario ya existe')
        return HttpResponse('claves incorrectas')
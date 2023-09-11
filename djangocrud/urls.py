"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tareas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('registrar/', views.registrar, name='registrar'),
    path('tareas/', views.tareas, name='tareas'),
    path('tareas/completadas/', views.listareascompletas, name='listareascompletas'),
    path('tareas/crear/', views.creartareas, name='creartareas'),
    path('tareas/<int:tarea_id>/', views.detalletareas, name='tareasdetalle'),
    path('tareas/<int:tarea_id>/completada', views.tareacompletada, name='tareacompletada'),
    path('tareas/<int:tarea_id>/eliminada', views.tareaeliminada, name='tareaeliminada'),
    path('cerrarsesion/', views.cerrarSesion, name='cerrarsesion'),
    path('iniciarsesion/', views.iniciarsesion, name='iniciarsesion'),
]

from django.forms import ModelForm
from .models import Tareas

class FormularioTareas(ModelForm):
    class Meta:
        model = Tareas
        fields = ['titulo','descripcion','importante']
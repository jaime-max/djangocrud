from django import forms
from .models import Tareas

class FormularioTareas(forms.ModelForm):
    class Meta:
        model = Tareas
        fields = ['titulo','descripcion','importante']
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control','placeholder': 'Ingrese un titulo'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control','placeholder': 'Ingrese una descripcion'}),
            'importante': forms.CheckboxInput(attrs={'class':'form-check-input text-center'}),
            #m-auto
        }
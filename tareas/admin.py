from django.contrib import admin
from .models import Tareas

class TareasAdmin(admin.ModelAdmin):
    readonly_fields = ("fechaCreacion", )
# Register your models here.
admin.site.register(Tareas, TareasAdmin)
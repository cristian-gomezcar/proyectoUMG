from django.contrib import admin
from .models import Docente, Estudiante, Curso, Carrera

admin.site.register(Docente)
admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Carrera)

# Register your models here.

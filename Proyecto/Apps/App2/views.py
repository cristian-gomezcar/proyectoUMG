from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from .forms import  DocenteForm, NotasForm, EstudianteForm, CursoForm, CarreraForm, NotasForm, RegistroForm
from .models import Docente, Notas, Estudiante, Curso, Carrera, Notas
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


# Create your views here.
class IndexView(TemplateView):  
	  template_name='Registrar/index2.html'

class registrarusuario(CreateView):
	  model = User
	  template_name = "Registrar/registrar.html"
	  form_class = RegistroForm
	  success_url=reverse_lazy('app2:Inicio')

class RegistrarDocentesView(CreateView):  
	  template_name='Registrar/Registrar_Docente.html'
	  model =Docente
	  form_class= DocenteForm
	  success_url=reverse_lazy('app2:Registrado')

class RegistrarEstudiantesView(CreateView):  
	  template_name='Registrar/Registrar_Estudiante.html'
	  model = Estudiante
	  form_class= EstudianteForm
	  success_url=reverse_lazy('app2:Registrado')	

class RegistrarCarrerasView(CreateView):  
	  template_name='Registrar/Registrar_Carrera.html'
	  model = Carrera
	  form_class= CarreraForm
	  success_url=reverse_lazy('app2:Registrado')

class RegistrarCursosView(CreateView):  
	  template_name='Registrar/Registrar_Curso.html'
	  model = Curso
	  form_class= CursoForm
	  success_url=reverse_lazy('app2:Registrado')

class NotasView(CreateView):  
	  template_name='Registrar/SubirNotas.html'
	  model = Notas
	  form_class = NotasForm
	  success_url=reverse_lazy('app2:Registrado')


class AdministrarView(TemplateView):  
	  template_name='Registrar/Administrar.html'

class registrarView(TemplateView):  
	  template_name='Registrar/Registros.html'


class registradoView(TemplateView):  
	  template_name='Registrar/Registrado.html'


class listarCarrerasView(ListView):
	  model = Carrera
	  template_name = 'listarRegistros/verCarrera.html'


class listarCursosView(ListView):
	  model = Curso
	  template_name = 'listarRegistros/VerCursos.html'


class listarDocentesView(ListView):
	  model = Docente
	  template_name = 'listarRegistros/verDocentes.html'

class listarEstudiantesView(ListView):
	  model = Estudiante
	  template_name = 'listarRegistros/VerEstudiantes.html'

class listarNotasView(ListView):
	  model = Notas
	  template_name = 'listarRegistros/VerNotas.html'

class DocenteUpdate(UpdateView):  
	  template_name='Actualizar/docentes.html'
	  model =Docente
	  form_class= DocenteForm
	  success_url=reverse_lazy('app2:listarDocentes')

class EstudiantesUpdate(UpdateView):  
	  template_name='Actualizar/estudiantes.html'
	  model =Estudiante
	  form_class= EstudianteForm
	  success_url=reverse_lazy('app2:listarEstudiantes')

class CursoUpdate(UpdateView):  
	  template_name='Actualizar/curso.html'
	  model =Curso
	  form_class= CursoForm
	  success_url=reverse_lazy('app2:listarCursos')

class CarreaUpdate(UpdateView):  
	  template_name='Actualizar/Carrera.html'
	  model = Carrera
	  form_class= CarreraForm
	  success_url=reverse_lazy('app2:listarCarreras')

class NotasUpdate(UpdateView):  
	  template_name='Actualizar/Notas.html'
	  model = Notas
	  form_class= NotasForm
	  success_url=reverse_lazy('app2:listarNotas')

class DocenteDelete(DeleteView):
	  model = Docente
	  template_name = 'Eliminar/docente.html'
	  success_url=reverse_lazy('app2:listarDocentes') 

class EstudianteDelete(DeleteView):
	  model = Estudiante
	  template_name = 'Eliminar/estudiante.html'
	  success_url=reverse_lazy('app2:listarEstudiantes') 

class CursoDelete(DeleteView):
	  model = Curso
	  template_name = 'Eliminar/curso.html'
	  success_url=reverse_lazy('app2:listarCursos') 

class CarreraDelete(DeleteView):
	  model = Carrera
	  template_name = 'Eliminar/carrera.html'
	  success_url=reverse_lazy('app2:listarCarreras') 

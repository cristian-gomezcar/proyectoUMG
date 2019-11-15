from django.forms import ModelForm
from django import forms
from .models import Docente, Estudiante, Curso, Carrera, Notas, grado
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EstudianteForm(ModelForm):
	class Meta:
		model = Estudiante
		fields = '__all__'

		labels={
			'idestudiante':'Codigo Estudiante',
			'pnombre':'Primer Nombre',
			'snombre':'Segundo Nombre',
			'pApellido':'Primer Apellido',
			'sApellido':'SegundoApellido',
			'idgrado':'Grado',
			'fNacimiento':'Fecha de Nacimiento',
			'direccion': 'Direccion',
			'correo':'Correo Electronico',
			'idcarrera':'Nombre de la Carrera',
			'iddocente':'Seleccione los Docentes del Alumno',

		}

		widgets = {
			'idestudiante':forms.NumberInput(attrs={'class':'form-control'}),
			'pnombre':forms.TextInput(attrs={'class':'form-control'}),
			'snombre': forms.TextInput(attrs={'class':'form-control'}),
			'pApellido': forms.TextInput(attrs={'class':'form-control'}),
			'sApellido': forms.TextInput(attrs={'class':'form-control'}),
			'idgrado': forms.Select(attrs={'class':'form-control'}),
			'fNacimiento': forms.SelectDateWidget(years=range(1950,2030), attrs={'class':'fecha'}),
			'direccion': forms.TextInput(attrs={'class':'form-control'}),
			'correo': forms.EmailInput(attrs={'class':'form-control'}),
			'idcarrera': forms.Select(attrs={'class':'form-control'}),
			'iddocente': forms.CheckboxSelectMultiple(),

		}

class DocenteForm(ModelForm):
	class Meta:
		model = Docente
		fields = '__all__'

		labels={
		
			'iddocente':'Codigo del Docente',
			'pnombre':'Primer Nombre',
			'snombre':'Segundo Nombre',
			'pApellido':'Primer Apellido',
			'sApellido':'SegundoApellido',
			'fNacimiento':'Fecha de Nacimiento',
			'direccion': 'Direccion',
			'correo':'Correo Electronico',
		}

		widgets = {
			'iddocente':forms.NumberInput(attrs={'class':'form-control'}),
			'pnombre':forms.TextInput(attrs={'class':'form-control'}),
			'snombre': forms.TextInput(attrs={'class':'form-control'}),
			'pApellido': forms.TextInput(attrs={'class':'form-control'}),
			'sApellido': forms.TextInput(attrs={'class':'form-control'}),
			'fNacimiento': forms.SelectDateWidget(years=range(1950,2030), attrs={'class':'fecha'}),
			'direccion': forms.TextInput(attrs={'class':'form-control'}),
			'correo': forms.EmailInput(attrs={'class':'form-control'}),

		}



class CarreraForm(ModelForm):
	class Meta:
		model = Carrera
		fields = '__all__'

		labels={
		    'idcarrera': 'Codigo de la Carrera',
		    'nombre': 'Nombre de la carrera',
		}

		widgets = {
			'idcarrera':forms.NumberInput(attrs={'class':'form-control'}),
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
		}

class GradoForm(ModelForm):
	class Meta:
		model = grado
		fields = '__all__'

		labels={
		    'idgrado': 'Codigo de grado',
		    'grado': 'grado',
		    'seccion': 'Seccion',
		}

		widgets = {
			'idgrado':forms.NumberInput(attrs={'class':'form-control'}),
			'grado':forms.NumberInput(attrs={'class':'form-control'}),
			'seccion':forms.TextInput(attrs={'class':'form-control'}),
		}

class CursoForm(ModelForm):
	class Meta:
		model = Curso
		fields = '__all__'

		labels={
		    'idcurso': 'Codigo del curso',
		    'idcarrera': 'Nombre de la carrera',
		    'iddocente': 'Nombre del docente',
		    'nombre':'nombre del curso',
		    'idgrado': 'Grado',
		}

		widgets = {
			'idcurso':forms.NumberInput(attrs={'class':'form-control'}),
			'idcarrera':forms.Select(attrs={'class':'form-control'}),
			'iddocente':forms.Select(attrs={'class':'form-control'}),
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'idgrado':forms.Select(attrs={'class':'form-control'}),
		}

class NotasForm(ModelForm):
	class Meta:
		model = Notas
		fields = '__all__'

		labels={
		    'nota': 'Ingrese la nota',
		    'idcurso': 'Seleccione el Curso',
		    'idcarrera': 'Seleccione la Carrera',
		    'iddocente': 'Codigo del Docente',
		    'idestudiante': 'Nombre del Estudiante',
		    'idgrado': 'Grado',
		}

		widgets = {
			'nota':forms.NumberInput(attrs={'class':'form-control'}),
			'idcurso':forms.Select(attrs={'class':'form-control'}),
			'idcarrera':forms.Select(attrs={'class':'form-control'}),
			'iddocente':forms.Select(attrs={'class':'form-control'}),
			'idestudiante':forms.Select(attrs={'class':'form-control'}),
			'idgrado':forms.Select(attrs={'class':'form-control'}),
		}

class RegistroForm(UserCreationForm):
	class Meta:
		model = User
		fields = [
			'username',
		    'first_name',
			'last_name',
			'email',
			]

		labels= {
		    'username':'Nombre de Usuario',
		    'first_name':'Nombre',
			'last_name':'Apellido',
			'email': 'Correo',
		}

		widgets={
			'username':forms.TextInput(attrs={'class':'form-control'}),
			'first_name':forms.TextInput(attrs={'class':'form-control'}),
			'last_name':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.EmailInput(attrs={'class':'form-control'}),

		}





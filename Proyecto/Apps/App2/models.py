from django.db import models

# Create your models here.

class Carrera(models.Model):
	idcarrera = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=25)

	def __str__ (self):
		return '{}'.format(self.nombre)

class grado(models.Model):
	idgrado = models.IntegerField(primary_key=True)
	grado = models.IntegerField()
	seccion = models.CharField(max_length=25)

	def __str__ (self):
		return '{} {}'.format(self.grado, self.seccion)


class Docente(models.Model):
	iddocente = models.IntegerField(primary_key=True)
	pnombre = models.CharField(max_length=25)
	snombre = models.CharField(max_length=25)
	pApellido = models.CharField(max_length=25)
	sApellido = models.CharField(max_length=25)
	fNacimiento = models.CharField(max_length=25)
	direccion= models.CharField(max_length=25)
	correo=models.EmailField(max_length=25)


	def __str__ (self):
		return '{} {}'.format(self.pnombre, self.pApellido)


class Estudiante(models.Model):
	idestudiante = models.IntegerField(primary_key=True)
	pnombre = models.CharField(max_length=25)
	snombre = models.CharField(max_length=25)
	pApellido = models.CharField(max_length=25)
	sApellido = models.CharField(max_length=25)
	fNacimiento= models.CharField(max_length=25)
	direccion= models.CharField(max_length=25)
	correo=models.EmailField(max_length=25)
	idcarrera= models.ForeignKey(Carrera, on_delete=models.CASCADE)
	iddocente=models.ManyToManyField(Docente)
	idgrado= models.ForeignKey(grado, on_delete=models.CASCADE)

	def __str__ (self):
		return '{} {}'.format(self.pnombre,self.pApellido)


class Curso(models.Model):
	idcurso = models.IntegerField(primary_key=True)
	idcarrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
	iddocente = models.ForeignKey(Docente, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=25)
	idgrado = models.ForeignKey(grado, on_delete=models.CASCADE)

	def __str__ (self):
		return '{}'.format(self.nombre)

class Notas(models.Model):
	nota = models.IntegerField();
	idcurso = models.ForeignKey(Curso, on_delete=models.CASCADE)
	idcarrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
	iddocente = models.ForeignKey(Docente, on_delete=models.CASCADE)
	idestudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
	idgrado= models.ForeignKey(grado, on_delete=models.CASCADE)

	def __str__ (self):
		return '{}'.format(self.nota)



"""PrimerProyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url,include
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import IndexView,registrarusuario, RegistrarDocentesView, RegistrarEstudiantesView, AdministrarView, RegistrarCarrerasView, RegistrarCursosView,registrarView, registradoView, NotasView, listarCarrerasView, listarCursosView, listarDocentesView, listarEstudiantesView,listarNotasView, DocenteUpdate, EstudiantesUpdate, CursoUpdate, CarreaUpdate,NotasUpdate, DocenteDelete, EstudianteDelete, CursoDelete, CarreraDelete
urlpatterns = [
    path('registrar/', login_required(registrarusuario.as_view()),name='registrar'),
    path('Inicio/', login_required(IndexView.as_view()),name='Inicio'),
    path('RegistrarDocentes/',login_required (RegistrarDocentesView.as_view()), name='RegistrarDocentes'),
    path('RegistrarEstudiantes/',login_required (RegistrarEstudiantesView.as_view()),name='RegistrarEstudiantes'),
    path('RegistrarCarrera/',login_required(RegistrarCarrerasView.as_view()),name='RegistrarCarrera'),
    path('RegistrarCurso/',login_required(RegistrarCursosView.as_view()),name='RegistrarCurso'),
    path('SubirNotas/',login_required(NotasView.as_view()),name='SubirNotas'),
    path('Administrar/',login_required (AdministrarView.as_view()),name='Administrar'),
    path('Registros/', login_required(registrarView.as_view()),name='Registros'),
    path('Registrado/', login_required(registradoView.as_view()),name='Registrado'),
    path('listarCarreras/',login_required (listarCarrerasView.as_view()),name='listarCarreras'),
    path('listarCursos/',login_required (listarCursosView.as_view()),name='listarCursos'),
    path('listarDocentes/',login_required (listarDocentesView.as_view()),name='listarDocentes'),
    path('listarEstudiantes/', login_required(listarEstudiantesView.as_view()),name='listarEstudiantes'),
    path('listarNotas/', login_required(listarNotasView.as_view()),name='listarNotas'),
    path('ActualizarDocente/<pk>',login_required(DocenteUpdate.as_view()),name='ActualizarDocente'),
    path('ActualizarEstudiante/<pk>',login_required(EstudiantesUpdate.as_view()),name='ActualizarEstudiante'),
    path('ActualizarCurso/<pk>',login_required(CursoUpdate.as_view()),name='ActualizarCurso'),
    path('ActualizarDocente/<pk>',login_required(DocenteUpdate.as_view()),name='ActualizarDocente'),
    path('ActualizarNotas/<pk>',login_required(NotasUpdate.as_view()),name='ActualizarNotas'),
    path('DocenteDelete/<pk>',login_required(DocenteDelete.as_view()),name='DocenteDelete'),
    path('EstudianteDelete/<pk>',login_required(EstudianteDelete.as_view()),name='EstudianteDelete'),
    path('CursoDelete/<pk>',login_required(CursoDelete.as_view()),name='CursoDelete'),
    path('CarreraDelete/<pk>',login_required(CarreraDelete.as_view()),name='CarreraDelete'),
]

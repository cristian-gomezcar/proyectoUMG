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
from .views import IndexView, DocentesView, GaleriaView, InformacionView, AcercaView, estdianteList
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
urlpatterns = [
    path('', IndexView.as_view()), 
    path('Inicio/', IndexView.as_view(),name='Inicio'),
    path('Docentes/', DocentesView.as_view(),name='Docentes'),
    path('Galeria/', GaleriaView.as_view(),name='Galeria'),
    path('Informacion/', estdianteList.as_view(),name='Informacion'),
    path('Acerca/',  estdianteList.as_view(),name='Acerca'),
    #path('registrar/', registrarusuario.as_view(),name='registrar'),
    path('login/', LoginView.as_view(template_name='Usuario/logiarse.html'),name = 'login'),

]

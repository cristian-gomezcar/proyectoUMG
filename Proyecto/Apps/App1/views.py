from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy


# Create your views here.
class IndexView(TemplateView):  
	  template_name='index.html'

class DocentesView(TemplateView):  
	  template_name='docentes.html'  

class GaleriaView(TemplateView):  
	  template_name='galeria.html'

class InformacionView(TemplateView):  
	  template_name='informacion.html'

class AcercaView(TemplateView):  
	  template_name='acerca.html'

class estdianteList(TemplateView): 
	  template_name='acerca.html'

#class registrarusuario(CreateView):
#	  model = User
#	  template_name = "Usuario/registrar.html"
#	  form_class = RegistroForm
#	  success_url=reverse_lazy('app1:Inicio')	 
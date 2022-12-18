from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from AppCamionetas.models import Camionetas
from django.urls import reverse_lazy
from AppInicio.views import imagen_avatar
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from AppCamionetas.models import Camionetas

# Create your views here.



def inicio(request):
    imagen_url = imagen_avatar(request)
    return render(request, 'AppCamionetas/index.html',{"imagen_url": imagen_url})


class CamionetaCreateView(LoginRequiredMixin, CreateView):

    model = Camionetas
    template_name = "AppCamionetas/camionetas.html"
    fields = "__all__"
    success_url = reverse_lazy("camionetas-listado")
    
class CamionetaListView(ListView):

    model = Camionetas
    template_name = "AppCamionetas/camionetas.html"

class CamionetasDetailView(DetailView):

    model = Camionetas
    template_name = "AppCamionetas/detalle.html"


class CamionetasDeleteView(LoginRequiredMixin, DeleteView):

    model = Camionetas
    success_url = reverse_lazy("camionetas-listado")

class CamionetasUpdateView(LoginRequiredMixin, UpdateView):

    model = Camionetas
    success_url = reverse_lazy("camionetas-listado")
    fields = "__all__"

def ConsultaCamionetas(request):

    if request.GET:
        marca_camioneta = request.GET.get("marca", "")
        
        if marca_camioneta == "":
            marcas = []
        else:
            marcas = Camionetas.objects.filter(marca__icontains=request.GET.get("marca"))
        return render(request, "AppCamionetas/buscar.html", {"listado_marcas": marcas})

    return render(request, "AppCamionetas/buscar.html", {"listado_marcas":[]})
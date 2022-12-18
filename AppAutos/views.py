from django.shortcuts import render
from AppInicio.views import imagen_avatar
from AppAutos.models import *
from AppAutos.forms import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home_autos(request):
    
    imagen_url = imagen_avatar(request)

    return render(request, 'AppAutos/index.html',{"imagen_url": imagen_url})


class AutoCreateView(LoginRequiredMixin, CreateView):

    model = CrearAnuncioDB
    template_name = "AppAutos/publicar.html"
    fields = "__all__"
    success_url = reverse_lazy("listado")
    
class AutoDeleteView(LoginRequiredMixin, DeleteView):

    model = CrearAnuncioDB
    success_url = reverse_lazy("listado")

class AutoUpdateView(LoginRequiredMixin, UpdateView):

    model = CrearAnuncioDB
    success_url = reverse_lazy("listado")
    fields = "__all__"


class AutoListView(ListView):

    model = CrearAnuncioDB
    template_name = "AppAutos/visualizar.html"


def buscarAuto(request):

    imagen_url = imagen_avatar(request)

    if request.GET:
        publicacion = CrearAnuncioDB.objects.filter(marca__icontains=request.GET["marca"])
        return render(request, 'AppAutos/buscar.html', {"publicacion_list": publicacion, "imagen_url": imagen_url})

    return render(request, 'AppAutos/buscar.html',{"publicacion_list": [], "imagen_url": imagen_url})
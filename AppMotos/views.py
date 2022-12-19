from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from AppMotos.models import Motos
from django.urls import reverse_lazy
from AppInicio.views import imagen_avatar
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from AppMotos.models import Motos

# Create your views here.



def inicio(request):
    imagen_url = imagen_avatar(request)
    return render(request, 'AppMotos/index.html',{"imagen_url": imagen_url})


class MotoCreateView(LoginRequiredMixin, CreateView):

    model = Motos
    template_name = "AppMotos/motos.html"
    fields = "__all__"
    success_url = reverse_lazy("motos-listado")
    
class MotoListView(ListView):

    model = Motos
    template_name = "AppMoto/motos.html"


class MotoDeleteView(LoginRequiredMixin, DeleteView):

    model = Motos
    success_url = reverse_lazy("motos-listado")

class MotoUpdateView(LoginRequiredMixin, UpdateView):

    model = Motos
    success_url = reverse_lazy("motos-listado")
    fields = "__all__"

def ConsultaMotos(request):

    if request.GET:
        marca_moto = request.GET.get("marca", "")
        
        if marca_moto == "":
            marcas = []
        else:
            marcas = Motos.objects.filter(marca__icontains=request.GET.get("marca"))
        return render(request, "AppMotos/buscar.html", {"listado_marcas": marcas})

    return render(request, "AppMotos/buscar.html", {"listado_marcas":[]})

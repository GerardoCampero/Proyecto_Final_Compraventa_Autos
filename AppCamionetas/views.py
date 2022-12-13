from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from AppCamionetas.models import Camionetas
from django.urls import reverse_lazy

# Create your views here.

def inicio(request):
    return render(request, "AppCamionetas/index.html")


class CamionetaCreateView(CreateView):

    model = Camionetas
    template_name = "AppCamionetas/camionetas.html"
    fields = "__all__"
    success_url = reverse_lazy("camionetas-listado")
class CamionetaListView(ListView):

    model = Camionetas
    template_name = "AppCamionetas/camionetas.html"

class CamionetasDeleteView(DeleteView):

    model = Camionetas
    success_url = reverse_lazy("camionetas-listado")

class CamionetasUpdateView(UpdateView):

    model = Camionetas
    success_url = reverse_lazy("camionetas-listado")
    fields = "__all__"
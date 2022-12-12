from django.shortcuts import render
from django.views.generic import CreateView, ListView
from AppCamionetas.models import Camionetas

# Create your views here.

def inicio(request):
    return render(request, "AppCamionetas/index.html")


class CamionetaCreateView(CreateView):

    model = Camionetas
    template_name = "AppCamionetas/camionetas.html"
    fields = "__all__"
    success_url = "AppCamionetas/index.html"

class CamionetaListView(ListView):

    model = Camionetas
    template_name = "AppCamionetas/camionetas.html"
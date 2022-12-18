from django.shortcuts import render
from AppInicio.views import imagen_avatar

# Create your views here.
def home_autos(request):
    
    imagen_url = imagen_avatar(request)

    return render(request, 'AppAutos/index.html',{"imagen_url": imagen_url})
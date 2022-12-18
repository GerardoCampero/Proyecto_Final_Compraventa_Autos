from django.shortcuts import render
from AppUsuarios.models import avatar
# Create your views here.


def home(request):
    
    imagen_url = imagen_avatar(request)

    return render(request, 'AppInicio/index.html',{"imagen_url": imagen_url})

def about(request):
    imagen_url = imagen_avatar(request)
    return render(request, 'AppInicio/about.html', {"imagen_url": imagen_url})


def imagen_avatar(request):
    
    if request.user.is_authenticated:
        imagen_model = avatar.objects.filter(user=request.user.id).order_by("-id")

        if len(imagen_model) > 0:
            imagen_url = imagen_model[0].imagen.url
        else:
            imagen_url = "/media/predet/avatar.jpg"  
                 
    else:
        imagen_url = ''

    return imagen_url


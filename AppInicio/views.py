from django.shortcuts import render
from AppUsuarios.models import avatar

# Create your views here.


def home(request):

    if request.user.is_authenticated:
        imagen_model = avatar.objects.filter(user=request.user.id).order_by("-id")[0]
        imagen_url = imagen_model.imagen.url
    else:
        imagen_url = ''

    return render(request, 'AppInicio/index.html',{"imagen_url": imagen_url})


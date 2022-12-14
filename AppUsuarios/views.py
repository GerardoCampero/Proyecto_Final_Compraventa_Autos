from django.shortcuts import render , redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login , authenticate 
from AppUsuarios.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from AppUsuarios.models import avatar
from AppInicio.views import imagen_avatar


# Create your views here.

def login(request):

    errors = ''

    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data

            user = authenticate(username=data["username"] , password=data["password"])

            if user is not None:
                auth_login(request, user)
                return redirect('inicio')
            else:
                return render(request, "AppUsuarios/login.html", {"form": formulario, "errors": "Usuario Inexistente"})
        else:
            return render(request, "AppUsuarios/login.html", {"form": formulario, "errors": formulario.errors})
    formulario = AuthenticationForm()
    return render(request, "AppUsuarios/login.html", {"form": formulario, "errors": errors})

def nuevo_usuario(request):

    formulario = UserRegisterForm()

    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
        else:
            return render(request, "AppUsuarios/create.html", {"form": formulario, "errors": formulario.errors})


    return render(request, "AppUsuarios/create.html", {"form": formulario})
    
@login_required
def editar_perfil(request):

    usuario = request.user

    imagen_url = imagen_avatar(request)

    if request.method == "POST":
        
        formulario = UserEditForm(request.POST)

    

        if formulario.is_valid():
            data = formulario.cleaned_data
            

            usuario.email = data["email"]
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]

            usuario.save()

            return redirect('inicio')
        else:
            return render(request,"AppUsuarios/edit.html", {"form": formulario, "errors": formulario.errors, "imagen_url": imagen_url} )


    else:
        formulario =  UserEditForm(initial = {"email": usuario.email, "first_name": usuario.first_name, "last_name": usuario.last_name, "imagen_url": imagen_url})
    
    return render(request,"AppUsuarios/edit.html", {"form": formulario,  "imagen_url": imagen_url})


@login_required
def agregar_avatar(request):

    imagen_url = imagen_avatar(request)
    
    if request.method == "POST":
        
        formulario = avatarFORM(request.POST, files=request.FILES)

        if formulario.is_valid():

            data = formulario.cleaned_data

            usuario =  request.user

            avatar_v = avatar(user=usuario, imagen=data["imagen"])
            
            avatar_v.save()

            return redirect('inicio')
        else:
            return render(request,"AppUsuarios/avatar.html", {"form": formulario, "errors":formulario.errors, "imagen_url": imagen_url})
    
    formulario = avatarFORM()

    return render(request,"AppUsuarios/avatar.html", {"form": formulario, "imagen_url": imagen_url})

    

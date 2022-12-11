from django.shortcuts import render , redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login , authenticate 
from AppUsuarios.forms import UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin

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
    

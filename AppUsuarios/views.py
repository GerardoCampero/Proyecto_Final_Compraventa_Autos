from django.shortcuts import render , redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login , authenticate 

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

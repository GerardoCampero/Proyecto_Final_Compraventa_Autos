from AppUsuarios.views import login
from django.urls import path

# Se declaran las rutas 

urlpatterns = [
    path("login/",login, name='login'), 
]
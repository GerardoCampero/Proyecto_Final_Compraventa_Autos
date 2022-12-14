from AppUsuarios.views import *
from django.urls import path
from django.contrib.auth.views import LogoutView

# Se declaran las rutas 

urlpatterns = [
    path("login/", login, name='login'), 
    path("create/", nuevo_usuario, name='create'),
    path("logout/", LogoutView.as_view(template_name="AppUsuarios/logout.html"), name='logout'),
    path("edit/" ,editar_perfil, name='edit'),
    path("avatar/",agregar_avatar, name='Add-avatar'),
]
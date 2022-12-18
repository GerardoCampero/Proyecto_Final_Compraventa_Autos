from django.urls import path
from AppInicio.views import home, about

# Se definan las urls de AppInicio

urlpatterns = [
    path('', home, name='home'), 
    path('inicio', home, name='inicio'),
    path('about', about, name='about') 
]
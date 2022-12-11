from django.urls import path
from AppInicio.views import home

# Se definan las urls de AppInicio

urlpatterns = [
    path('', home, name='home'), 
]
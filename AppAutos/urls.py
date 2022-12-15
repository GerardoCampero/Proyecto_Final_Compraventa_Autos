from AppAutos.views import *
from django.urls import path

urlpatterns = [
    path('autos/', home_autos, name='autos'), 
 
]

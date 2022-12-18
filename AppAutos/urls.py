from AppAutos.views import *
from django.urls import path

urlpatterns = [
    path('autos/', home_autos, name='autos'), 
    path('publicar/', AutoCreateView.as_view(), name='publicar'),
    path('listado/', AutoListView.as_view(), name='listado'),
    path('eliminar/<pk>', AutoDeleteView.as_view(), name='eliminar'),
    path('editar/<pk>', AutoUpdateView.as_view(), name='editar'),
]

from django.urls import path
from AppMotos.views import *

urlpatterns = [
    path('motos_inicio/', inicio, name="motos-inicio"),
    path('motos/', MotoCreateView.as_view(), name="motos"),
    path('listado/', MotoListView.as_view(), name="motos-listado"),
    path('motos/borrar/<pk>', MotoDeleteView.as_view(), name="motos-eliminar"),
    path('motos/editar/<pk>', MotoUpdateView.as_view(), name="motos-editar"),
    path('buscar/', ConsultaMotos, name="motos-buscar" )
]
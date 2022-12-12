
# urls.py agregado por Rogers dentro de la app

from django.urls import path
from AppCamionetas.views import *

urlpatterns = [
    path('', inicio, name="camionetas-inicio"),
    path('camionetas/', CamionetaCreateView.as_view(), name="camionetas"),
    path('camionetas/listado', CamionetaListView.as_view(), name="camionetas-listado")
]
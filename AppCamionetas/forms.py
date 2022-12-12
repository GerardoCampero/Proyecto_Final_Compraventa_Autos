from django import forms
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from AppCamionetas import models

class CrearCamioneta(CreateView):
    marca = self
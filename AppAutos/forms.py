from django import forms

# Se definen los formularios 

class CrearAnuncioForm(forms.Form):

    marca = forms.CharField(max_length=100)
    modelo = forms.CharField(max_length=100)
    kilometros = forms.IntegerField()
    anio = forms.IntegerField()
    precio = forms.FloatField()
    foto = forms.ImageField()
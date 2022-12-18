from django.db import models

# Create your models here.


class CrearAnuncioDB(models.Model):
    
    
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anio = models.IntegerField()
    kilometros = models.IntegerField()
    precio = models.FloatField()
    foto = models.ImageField(upload_to="Fotos")
    

    def __str__(self) -> str:
        return f"{self.marca} - {self.modelo}: ${self.precio}"
    
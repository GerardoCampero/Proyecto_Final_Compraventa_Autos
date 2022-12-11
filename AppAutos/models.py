from django.db import models

# Create your models here.


class AutosDB(models.Model):
    
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    kilometros = models.IntegerField()
    precio = models.FloatField()
    foto = models.ImageField(upload_to="Fotos")

    def __str__(self) -> str:
        return f"{self.marca} - {self.modelo}: ${self.precio}"
    pass
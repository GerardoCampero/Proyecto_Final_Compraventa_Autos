from django.db import models

class Motos(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio_fabricacion = models.IntegerField()
    kilometraje = models.IntegerField()
    precio = models.FloatField()
    foto = models.ImageField(upload_to="motos")

    def __str__(self):
        return f"Marca: {self.marca} || Modelo: {self.modelo} ||Año: {self.anio_fabricacion} || Kilometraje: {self.kilometraje} || Precio:$ {self.precio} || Foto: {self.foto}"

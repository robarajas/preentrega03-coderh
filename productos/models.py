from django.db import models

# Create your models here.
class Producto(models.Model):
    sku = models.CharField(max_length=25)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
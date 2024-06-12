from django.db import models

# Create your models here.
class Direccion(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150)
    ciudad = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=10)
    
    def __str__(self):
        return self.nombre
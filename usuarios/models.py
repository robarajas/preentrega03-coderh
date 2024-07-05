from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DatosExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Relacion uno a uno con la tabla User - FK
    rol_usuario = models.CharField(max_length=1,  choices=(('C', 'Comprador'), ('V', 'Vendedor')), default='C')
    genero = models.CharField(max_length=1, choices=(('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')), default='O')
    fecha_nacimiento = models.DateField()
    avatar = models.ImageField(null=True, upload_to='avatares', blank=True)

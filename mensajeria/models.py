from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Canal(models.Model):
  asunto = models.CharField(max_length=100, default='Sin Asunto')
  usuario_creador = models.ForeignKey(User, on_delete=models.DO_NOTHING)
  fecha_creacion = models.DateTimeField(auto_now_add=True)
  
class CanalUsuarios(models.Model):
  canal = models.ForeignKey(Canal, on_delete=models.CASCADE)
  usuario = models.ForeignKey(User, on_delete=models.CASCADE)
  ultimo_mensaje_leido = models.IntegerField(default=0)
  fecha_registro = models.DateTimeField(auto_now_add=True)
  
class Mensaje(models.Model):
  mensaje = models.TextField()
  canal = models.ForeignKey(Canal, on_delete=models.CASCADE)
  usuario_emisor = models.ForeignKey(User, on_delete=models.CASCADE)
  fecha_registro = models.DateTimeField(auto_now_add=True)
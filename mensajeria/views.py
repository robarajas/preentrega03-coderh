from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from mensajeria.forms import CrearCanalForm, EnviarMensajeForm
from .models import Canal, CanalUsuarios, Mensaje

# Create your views here.
@login_required
def verCanales(request):
  user = request.user
  print(user, 'USUARIO')
  canales = Canal.objects.filter(canalusuarios__usuario=user)
  print(canales, 'CANALES')
  return render(request, 'mensajeria/canales.html', {'canales': canales})

@login_required
def crearCanal(request):
  loginUser = request.user
  formulario = CrearCanalForm()
  if request.method == 'POST':
    formulario = CrearCanalForm(request.POST)
    if formulario.is_valid():
      data = formulario.cleaned_data
      print(data, 'DATA FORM')
      asunto = data['asunto']
      usuario = data['usuario']
      mensaje = data['mensaje']
      canal = Canal.objects.create(asunto=asunto, usuario_creador=usuario)
      CanalUsuarios.objects.create(canal=canal, usuario=usuario)
      CanalUsuarios.objects.create(canal=canal, usuario=loginUser)
      mensaje = Mensaje.objects.create(mensaje=mensaje, canal=canal, usuario_emisor=loginUser)
      return redirect('canales')
  return render(request, 'mensajeria/crear_canal.html', {'formulario': formulario,})

@login_required
def verCanal(request, id):
  formulario = EnviarMensajeForm()
  canal = Canal.objects.get(id=id)
  userlogged = request.user
  mensajes = Mensaje.objects.filter(canal=canal)
  if request.method == 'POST':
    formulario = EnviarMensajeForm(request.POST)
    if formulario.is_valid():
      data = formulario.cleaned_data
      mensaje = data['mensaje']
      Mensaje.objects.create(mensaje=mensaje, canal=canal, usuario_emisor=request.user)
      return redirect('ver_canal', id=id)
  return render(request, 'mensajeria/ver_canal.html', {'canal': canal, 'mensajes': mensajes, 'formulario': formulario, 'userlogged': userlogged})
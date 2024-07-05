from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as djangoLogin
from usuarios.forms import FormularioRegistro, EditarPerfilForm
from django.contrib.auth.decorators import login_required
from usuarios.models import DatosExtra

# Create your views here.
def login(request):
  formulario = AuthenticationForm()
  print(request, 'REQUEST')
  print(request.method, 'MEHTOD')
  if request.method == 'POST':
    formulario = AuthenticationForm(data=request.POST)
    if formulario.is_valid():
      print('FORMULARIO VALIDO')
      data = formulario.cleaned_data
      username = data['username']
      password = data['password']
      user = authenticate(request, username=username, password=password)
      djangoLogin(request, user)
      DatosExtra.objects.get_or_create(user=user)
      return redirect('main')
    else:
      print('FORMULARIO INVALIDO')
  return render(request, 'usuarios/login.html', {'formulario': formulario})

def registro(request):
  formulario = FormularioRegistro()
  if request.method == 'POST':
    formulario = FormularioRegistro(request.POST)
    if formulario.is_valid():
      user = formulario.save()
      datos_formulario = formulario.cleaned_data
      genero = datos_formulario['genero']
      rol_usuario = datos_formulario['rol_usuario']
      fecha_nacimiento = datos_formulario['fecha_nacimiento']
      DatosExtra.objects.create(user=user, genero=genero, rol_usuario=rol_usuario, fecha_nacimiento=fecha_nacimiento)
      return redirect('login')
  return render(request, 'usuarios/registro_usuario.html', { 'formulario': formulario })

@login_required
def editarPerfil(request):
  avatar = request.user.datosextra.avatar
  datosextra = DatosExtra.objects.get(user=request.user)
  context = { 'avatar': avatar, 'genero': datosextra.genero, 'rol_usuario': datosextra.rol_usuario, 'fecha_nacimiento': datosextra.fecha_nacimiento }
  formulario = EditarPerfilForm(initial=context, instance=request.user)
  if request.method == 'POST':
    formulario = EditarPerfilForm(request.POST, request.FILES, instance=request.user)
    if formulario.is_valid():
      hasNewAvatar = formulario.cleaned_data['avatar']
      if hasNewAvatar != None:
        datosextra.avatar = formulario.cleaned_data['avatar']
      datosextra.rol_usuario = formulario.cleaned_data['rol_usuario']
      datosextra.genero = formulario.cleaned_data['genero']
      datosextra.fecha_nacimiento = formulario.cleaned_data['fecha_nacimiento']
      datosextra.save()
      formulario.save()
      return redirect('editar_perfil')
  return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario, 'avatar': datosextra.avatar})


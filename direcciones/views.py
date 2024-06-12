from django.shortcuts import render, redirect
from direcciones.models import Direccion
from direcciones.forms import DireccionForm

# Create your views here.
def listado_direcciones(request):
  direcciones = Direccion.objects.all()
  return render(request, 'direcciones/listado_direcciones.html', {'direcciones': direcciones})

def agregar_direccion(request):
  formulario = DireccionForm();
  if request.method == 'POST':
    formulario = DireccionForm(request.POST)
    if formulario.is_valid():
      datos = formulario.cleaned_data
      direccion = Direccion(nombre=datos['nombre'], direccion=datos['direccion'], ciudad=datos['ciudad'], codigo_postal=datos['codigo_postal'])
      direccion.save()
      return redirect('listado_direcciones')
  return render(request, 'direcciones/agregar_direcciones.html', {'formulario': formulario})
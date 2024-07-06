from django.shortcuts import render, redirect
from direcciones.models import Direccion
from direcciones.forms import DireccionForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
@login_required
def listado_direcciones(request):
  direcciones = Direccion.objects.all()
  return render(request, 'direcciones/listado_direcciones.html', {'direcciones': direcciones})

@login_required
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

class EditarDireccion(LoginRequiredMixin, UpdateView):
  model = Direccion
  fields = ['nombre', 'direccion', 'ciudad', 'codigo_postal']
  template_name = 'direcciones/editar_direccion.html'
  success_url = reverse_lazy('listado_direcciones')
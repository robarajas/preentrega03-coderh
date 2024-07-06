from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from productos.models import Producto
from django.views.generic import DetailView
from django.views.generic.edit import DeleteView
from productos.forms import CrearProducto, BuscarProducto, EditarProductoFormulario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def catalogo(request):
    isAuthenticated = request.user.is_authenticated
    username = None
    formularioBusqueda = BuscarProducto(request.GET)
    if formularioBusqueda.is_valid():
        nombre = formularioBusqueda.cleaned_data['nombre']
        products_list = Producto.objects.filter(nombre__icontains=nombre)
    return render(request, 'productos/catalogo.html', {'productos': products_list, 'isAuthenticated': isAuthenticated, 'username': username, 'formularioBusqueda': formularioBusqueda})

@login_required
def agregar_producto(request):
    formulario = CrearProducto()
    if request.method == 'POST':
        formulario = CrearProducto(request.POST, request.FILES)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            producto = Producto(sku=datos['sku'], nombre=datos['nombre'], precio=datos['precio'], descripcion=datos['descripcion'], imagen=datos['imagen'])
            producto.save()
            return redirect('catalogo')
    return render(request, 'productos/agregar.html', {'formulario': formulario})
  
class VerProducto(DetailView):
  model = Producto
  template_name = 'productos/detalles_producto.html'
  
class EliminarProducto(LoginRequiredMixin, DeleteView):
  model = Producto
  template_name = 'productos/eliminar_producto.html'
  success_url = reverse_lazy('catalogo')

@login_required
def editarProducto(request, id):
  producto = Producto.objects.get(id=id)
  formulario = EditarProductoFormulario(initial={'sku': producto.sku, 'nombre': producto.nombre, 'precio': producto.precio, 'descripcion': producto.descripcion, 'imagen': producto.imagen})
  if request.method == 'POST':
    formulario = EditarProductoFormulario(request.POST, request.FILES)
    if formulario.is_valid():
      params = formulario.cleaned_data
      hasNewImage = formulario.cleaned_data['imagen']
      if hasNewImage != None:
        producto.imagen = params['imagen']
      producto.sku = params['sku']
      producto.nombre = params['nombre']
      producto.precio = params['precio']
      producto.descripcion = params['descripcion']
      producto.save()
      return redirect('catalogo')
  return render(request, 'productos/editar_producto.html', {'formulario': formulario, 'producto': producto})
  
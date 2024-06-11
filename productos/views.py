from django.shortcuts import render, redirect
from productos.models import Producto
from productos.forms import CrearProducto

# Create your views here.
def catalogo(request):
    products_list = Producto.objects.all()
    return render(request, 'productos/catalogo.html', {'productos': products_list })

def agregar_producto(request):
    # cuando se envían parametros con formularios, se reciben en el request
    # print(request.GET, 'REQUEST') # Así se reciben los parámetros querystring como diccionarios
    # Si vamos a crear un producto con los valores recibidos, asegurarnos que sea con POST
    
    # Version donde se usa formulario de HTML
    # if request.method == 'POST':
    #     sku = request.POST.get('sku')
    #     nombre = request.POST.get('nombre')
    #     precio = request.POST.get('precio')
    #     descripcion = request.POST.get('descripcion')
    #     # Crear un nuevo producto
    #     producto = Producto(sku=sku, nombre=nombre, precio=precio, descripcion=descripcion)
    #     producto.save()
    #     return render(request, 'productos/catalogo.html', {'agregado': True})
    # return render(request, 'productos/agregar.html')
    
    # Versión donde se usa formulario de Django
    # Se inicializa el formulario antes del post para mostrar valores en inputs cuando falla
    formulario = CrearProducto()
    
    if request.method == 'POST':
        formulario = CrearProducto(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            producto = Producto(sku=datos['sku'], nombre=datos['nombre'], precio=datos['precio'], descripcion=datos['descripcion'])
            producto.save()
            return redirect('catalogo')
    return render(request, 'productos/agregar.html', {'formulario': formulario})
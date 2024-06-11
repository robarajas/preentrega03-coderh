from django.shortcuts import render
from productos.models import Producto

# Create your views here.
def catalogo(request):
    products_list = Producto.objects.all()
    return render(request, 'productos/catalogo.html', {'productos': products_list })
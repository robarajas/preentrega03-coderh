from django import forms

class CrearProducto(forms.Form):
  sku = forms.CharField(label='SKU', max_length=25)
  nombre = forms.CharField(label='Nombre', max_length=100)
  precio = forms.DecimalField(label='Precio')
  descripcion = forms.CharField(label='Descripción', widget=forms.Textarea(attrs={"rows":"3"}))
  imagen = forms.ImageField(label='Imagen', required=False)
    
class BuscarProducto(forms.Form):
  nombre = forms.CharField(label='Nombre del producto', max_length=100, required=False)
  
class EditarProductoFormulario(CrearProducto):
  ...
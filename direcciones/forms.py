from django import forms

class DireccionForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    direccion = forms.CharField(label='Dirección', max_length=150)
    ciudad = forms.CharField(label='Ciudad', max_length=50)
    codigo_postal = forms.CharField(label='Código Postal', max_length=10)
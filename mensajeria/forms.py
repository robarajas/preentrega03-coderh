from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth.models import User

class CrearCanalForm(forms.Form):
  asunto = forms.CharField(label='Asunto', max_length=20)
  usuario = forms.ModelChoiceField(queryset=User.objects.all(), label='Usuario')
  mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea(attrs={"rows":"3"}))

class EnviarMensajeForm(forms.Form):
  mensaje = forms.CharField(label='Nuevo Mensaje', widget=forms.Textarea(attrs={"rows":"3"}))
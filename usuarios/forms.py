from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class FormularioRegistro(UserCreationForm):
  email = forms.EmailField()
  password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
  password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
  rol_usuario = forms.ChoiceField(label='Tipo de usuario', choices=(('C', 'Comprador'), ('V', 'Vendedor')))
  genero = forms.ChoiceField(label='Género', choices=(('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')))
  fecha_nacimiento = forms.DateField(label='Fecha de nacimiento', widget=forms.SelectDateWidget(years=range(1990, 2010)))
  
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']
    help_texts = { key: '' for key in fields }

class EditarPerfilForm(UserChangeForm):
  password = None
  email = forms.EmailField
  first_name = forms.CharField(label='Nombre', max_length=20)
  last_name = forms.CharField(label='Apellido', max_length=25)
  rol_usuario = forms.ChoiceField(label='Tipo de usuario', choices=(('C', 'Comprador'), ('V', 'Vendedor')))
  genero = forms.ChoiceField(label='Género', choices=(('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')))
  fecha_nacimiento = forms.DateField(label='Fecha de nacimiento', widget=forms.SelectDateWidget(years=range(1990, 2010)))
  avatar = forms.ImageField(label='Avatar', required=False)
  
  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'email', 'rol_usuario', 'genero', 'fecha_nacimiento', 'avatar']
    help_texts = { key: '' for key in fields }
  
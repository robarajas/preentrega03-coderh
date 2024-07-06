from django.urls import path
from . import views

urlpatterns = [
  path('', views.verCanales, name='canales'),
  path('crear', views.crearCanal, name='crear_canal'),
  path('canal/<int:id>', views.verCanal, name='ver_canal'),
]
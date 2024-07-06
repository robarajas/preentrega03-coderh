from django.urls import path
from direcciones import views

urlpatterns = [
  path('', views.listado_direcciones, name='listado_direcciones'),
  path('agregar/', views.agregar_direccion, name='agregar_direccion'),
  path('editar/<int:pk>/', views.EditarDireccion.as_view(), name='editar_direccion'),
]

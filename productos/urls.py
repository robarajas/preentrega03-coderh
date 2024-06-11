from django.urls import path
from productos import views

urlpatterns = [
  path('', views.catalogo, name='catalogo'),
  path('agregar/', views.agregar_producto, name='agregar_producto')
]

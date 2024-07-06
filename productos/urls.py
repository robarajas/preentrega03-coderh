from django.urls import path
from productos import views

urlpatterns = [
  path('', views.catalogo, name='catalogo'),
  path('agregar/', views.agregar_producto, name='agregar_producto'),
  path('detalles/<int:pk>/', views.VerProducto.as_view(), name='detalles_producto'),
  path('editar/<int:id>', views.editarProducto, name='editar_producto'),
  path('eliminar/<int:pk>/', views.EliminarProducto.as_view(), name='eliminar_producto'),
]

from django.urls import path
from django.contrib.auth.views import LogoutView
from usuarios import views

urlpatterns = [
  path('login/', views.login, name='login'),
  path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
  path('registro/', views.registro, name='registro')
]

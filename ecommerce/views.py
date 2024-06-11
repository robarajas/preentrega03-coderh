from django.shortcuts import render

# Vistas principales
def main(request):
  return render(request, 'main/inicio.html')
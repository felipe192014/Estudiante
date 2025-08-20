from django.shortcuts import render
from .models import Programa

def lista_programas(request):
    programas = Programa.objects.all()
    return render(request, "programas.html", {"programas": programas})
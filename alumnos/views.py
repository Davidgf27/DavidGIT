from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hola David, este es el home de tu proyecto</h1><a href='saludo'>Ir a saludo</a>")

def saludo(request):
    return HttpResponse("<h1>Hola David, bienvenido al mundo Django</h1><a href='home'>Ir a saludo</a>")
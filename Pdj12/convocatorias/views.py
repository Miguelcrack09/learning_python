from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def hola(request):
    return HttpResponse("Hola Clase")

def saludo(request):
    laClase = "S20"
    elSaludo = f"Hola Clase{laClase}"
    return HttpResponse(elSaludo)
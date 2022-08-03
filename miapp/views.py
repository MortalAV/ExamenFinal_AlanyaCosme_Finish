from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from miapp import models

# Create your views here.
layout = """"""

def integrantes(request):
    integrantes = ['Alanya Villar Joel Edwin','Cosme Hernandez Carlos Daniel']
    return render(request, 'integrantes.html', {
        'titulo':'Integrantes del proyecto',
        'integrantes':integrantes
    })

def inicio(request):
    return render(request, 'inicio.html', {
        'titulo':'Bienvenidos',
        'mensaje':'Proyecto para el Examen Final (EF)'
    })

def crearProducto(request):
    return render(request, 'crearProductos.html' ,{

    })

def crearCurso(request):
    return render(request, 'crearCursos.html' ,{
        
    })
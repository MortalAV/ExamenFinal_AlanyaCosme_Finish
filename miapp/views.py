from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from miapp import models
from miapp.models import Producto, Curso

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
    producto = Producto(
                        codigo = "54551544",
                        nombre = "Pedro",
                        precio_compra = 40.70,
                        precio_venta = 50.50,
                        Fecha_compra = "2022-08-03",
                        Fecha_registro = True,
                        estado = "A"
 )
    producto.save()
    return HttpResponse (f"<h1>Producto registrado:</h1> "+
    f"<br> <b>Código:</b> {producto.codigo} <br> <b>Nombre:</b> {producto.nombre} <br> <b>Precio de Compra:</b> {producto.precio_compra} <br> "+
    f"<b>Precio de venta:</b> {producto.precio_venta} <br> <b>Fecha de Compra:</b> {producto.Fecha_compra} <br><b>Fecha de Registro:</b> "+
    f" {producto.Fecha_registro} <br> <b>Estado:</b> {producto.estado}")

def crearCurso(request):
    curso = Curso(
                        codigo = "98944",
                        nombre = "pHYTON",
                        horas = 3,
                        creditos = 4,
                        Fecha_registro = True,
                        estado = "A"
 )
    curso.save()
    return HttpResponse (f"<h1>Curso registrado:</h1> "+
    f"<br> <b>Código:</b> {curso.codigo} <br> <b>Nombre:</b> {curso.nombre} <br> <b>Horas:</b> {curso.horas} <br> "+
    f"<b>Créditos:</b> {curso.creditos} <br> <b>Fecha de Registro:</b> "+
    f" {curso.Fecha_registro} <br> <b>Estado:</b> {curso.estado}") 
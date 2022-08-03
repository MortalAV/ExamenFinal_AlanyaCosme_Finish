from django.db import models

# Create your models here.

class Producto(models.Model):
    codigo = models.TextField(max_length=12)
    nombre = models.TextField()
    precio_compra = models.FloatField()
    precio_venta = models.FloatField()
    Fecha_compra = models.DateField()
    Fecha_registro = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=1)

class Curso(models.Model):
    codigo = models.TextField(max_length=12)
    nombre = models.TextField()
    horas = models.IntegerField()
    creditos = models.IntegerField()
    Fecha_registro = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=1)
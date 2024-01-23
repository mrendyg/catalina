from django.db import models
from users.models import User
from django import forms

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    
    class Meta:
        db_table = 'Marca'

class Modelo(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    tipo = models.CharField(max_length=50, null=True)
    anio = models.IntegerField(null=True, blank=True)


    class Meta:
        db_table = 'Modelo'

class Producto(models.Model):
    codigo = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    #modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    cantidad_stock = models.IntegerField(null=True, blank=True, default=0)
    imagen = models.ImageField(upload_to='./media/5596.jpg', null=True, blank=True)
    
    class Meta:
        db_table = 'Producto'

class Review(models.Model):
    product = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'Review'


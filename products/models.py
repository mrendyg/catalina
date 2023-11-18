from django.db import models
from users.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    
    class Meta:
        db_table = 'Categoria'

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el usuario
    
    class Meta:
        db_table = 'Producto'

class Review(models.Model):
    product = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
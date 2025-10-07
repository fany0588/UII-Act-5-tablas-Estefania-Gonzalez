from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre_producto = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre_producto}"
    
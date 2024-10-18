from django.db import models

class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    ingredientes = models.TextField()
    instrucciones = models.TextField()
    categoria = models.CharField(max_length=50, default='Sin asignar')  # Campo para clasificar la receta

    def __str__(self):
        return self.titulo



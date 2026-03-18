from django.db import models

class Cabana(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio_por_noche = models.IntegerField()
    capacidad_personas = models.IntegerField()
    cantidad_habitaciones = models.IntegerField(default=1)
    cantidad_banos = models.IntegerField(default=1)
    tiene_cocina = models.BooleanField(default=True)
    tiene_wifi = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='cabanas/', null=True, blank=True)

    def __str__(self):
        return self.nombre
from django.db import models

class Cabana(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    capacidad_personas = models.IntegerField()
    cantidad_habitaciones = models.IntegerField()
    cantidad_banos = models.IntegerField()
    imagen = models.ImageField(upload_to="cabanas/", null=True, blank=True)

    # --- Amenidades Básicas que ya tenías ---
    tiene_cocina = models.BooleanField(default=False)
    tiene_wifi = models.BooleanField(default=False)

    # --- NUEVAS AMENIDADES ---
    tiene_tv = models.BooleanField(default=False, verbose_name="¿Tiene Televisión?")
    tiene_aire_acondicionado = models.BooleanField(
        default=False, verbose_name="¿Tiene Aire Acondicionado/Calefacción?"
    )
    tiene_estacionamiento = models.BooleanField(
        default=False, verbose_name="¿Estacionamiento Privado?"
    )
    tiene_parrilla = models.BooleanField(
        default=False, verbose_name="¿Tiene Zona de Parrilla/Asados?"
    )
    acepta_mascotas = models.BooleanField(
        default=False, verbose_name="¿Acepta Mascotas (Pet Friendly)?"
    )

    def __str__(self):
        return self.nombre


class ImagenCabana(models.Model):
    # La ForeignKey conecta esta imagen con una cabaña específica.
    cabana = models.ForeignKey(
        Cabana, on_delete=models.CASCADE, related_name="imagenes"
    )

    # Aquí se guardarán las fotos extra de la galería
    imagen = models.ImageField(upload_to="galeria_cabanas/")

    def __str__(self):
        return f"Imagen de {self.cabana.nombre}"

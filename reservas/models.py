from django.db import models

class Cabana(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio_por_noche = models.IntegerField()
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


class Reserva(models.Model):
    # Relación: Una cabaña puede tener muchas reservas
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE, related_name='reservas')
    
    # Datos del cliente
    nombre_huesped = models.CharField(max_length=100, verbose_name="Nombre del Huésped")
    email_huesped = models.EmailField(verbose_name="Correo Electrónico")
    telefono_huesped = models.CharField(max_length=20, verbose_name="Teléfono")
    
    # Datos de la estadía
    fecha_llegada = models.DateField()
    fecha_salida = models.DateField()
    cantidad_personas = models.IntegerField()
    precio_total = models.IntegerField()
    
    # Metadatos
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    
    # Opciones de estado de la reserva
    ESTADOS_RESERVA = (
        ('pendiente', 'Pendiente (Por pagar/confirmar)'),
        ('confirmada', 'Confirmada y Pagada'),
        ('cancelada', 'Cancelada'),
    )
    estado = models.CharField(max_length=20, choices=ESTADOS_RESERVA, default='pendiente')

    def __str__(self):
        return f"Reserva #{self.id} - {self.cabana.nombre} ({self.fecha_llegada} al {self.fecha_salida})"
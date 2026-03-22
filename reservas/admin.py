from django.contrib import admin
from .models import Cabana, ImagenCabana, Reserva

# 1. Creamos el "Inline" para las imágenes
class ImagenCabanaInline(admin.TabularInline):
    model = ImagenCabana
    extra = 5  # Te mostrará 5 espacios vacíos por defecto para subir fotos rápidamente

# 2. Personalizamos cómo se ve la Cabaña en el administrador
class CabanaAdmin(admin.ModelAdmin):
    # Le decimos que incluya el formulario de imágenes dentro de la cabaña
    inlines = [ImagenCabanaInline] 

# Registramos el modelo con su nueva configuración
admin.site.register(Cabana, CabanaAdmin)

# Registramos el modelo de reservas
@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    # Estas son las columnas que verás en el panel de administrador
    list_display = ('id', 'cabana', 'nombre_huesped', 'fecha_llegada', 'fecha_salida', 'estado', 'precio_total')
    list_filter = ('estado', 'fecha_llegada') # Para poder filtrar rápidamente
    search_fields = ('nombre_huesped', 'email_huesped') # Para buscar clientes
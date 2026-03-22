from django.shortcuts import render, get_object_or_404
# IMPORTANTE: Asegúrate de importar también el modelo Reserva
from .models import Cabana, Reserva 

def home(request):
    return render(request, 'reservas/index.html')

def resultados(request):
    # Capturamos los datos del formulario
    llegada = request.GET.get('llegada', '')
    salida = request.GET.get('salida', '')
    personas = request.GET.get('personas', 1)
    habitaciones = request.GET.get('habitaciones', 1)

    # 1. Filtro inicial por capacidad (tu código original)
    cabanas = Cabana.objects.filter(
        capacidad_personas__gte=personas,
        cantidad_habitaciones__gte=habitaciones
    )
    
    # 2. NUEVO: Filtro inteligente de disponibilidad de fechas
    if llegada and salida:
        cabanas = cabanas.exclude(
            # Solo consideramos las reservas que importan
            reservas__estado__in=['pendiente', 'confirmada'], 
            
            # Condición de choque: La reserva existente entra ANTES de que yo me vaya
            # Y sale DESPUÉS de que yo llegue.
            reservas__fecha_llegada__lt=salida,  
            reservas__fecha_salida__gt=llegada   
        ).distinct() # distinct() es clave para no mostrar la misma cabaña dos veces

    contexto = {
        'cabanas': cabanas,
        'llegada': llegada,
        'salida': salida,
        'personas': personas,
        'habitaciones': habitaciones,
    }
    return render(request, 'reservas/resultados.html', contexto)

def detalle_cabana(request, cabana_id):
    # Buscamos la cabaña por su ID. Si no existe, muestra error 404.
    cabana = get_object_or_404(Cabana, id=cabana_id)
    return render(request, 'reservas/detalle.html', {'cabana': cabana})
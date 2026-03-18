from django.shortcuts import render, get_object_or_404
from .models import Cabana

def home(request):
    return render(request, 'reservas/index.html')

def resultados(request):
    llegada = request.GET.get('llegada', '')
    salida = request.GET.get('salida', '')
    personas = request.GET.get('personas', 1)
    habitaciones = request.GET.get('habitaciones', 1)

    cabanas = Cabana.objects.filter(
        capacidad_personas__gte=personas,
        cantidad_habitaciones__gte=habitaciones
    )
    
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
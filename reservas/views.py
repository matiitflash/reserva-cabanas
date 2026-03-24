from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
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

def checkout(request, cabana_id):
    cabana = get_object_or_404(Cabana, id=cabana_id)
    
    # 1. Recuperamos las fechas que vienen en la URL (ej: ?llegada=2023-10-01&salida=2023-10-05)
    llegada_str = request.GET.get('llegada', '')
    salida_str = request.GET.get('salida', '')
    personas = request.GET.get('personas', 1)

    noches = 0
    precio_total = 0
    fecha_llegada_obj = None
    fecha_salida_obj = None

    # 2. Calculamos las noches y el total si las fechas existen
    if llegada_str and salida_str:
        formato = "%Y-%m-%d" # Formato estándar de inputs type="date"
        try:
            fecha_llegada_obj = datetime.strptime(llegada_str, formato).date()
            fecha_salida_obj = datetime.strptime(salida_str, formato).date()
            
            # Restamos las fechas para obtener los días
            noches = (fecha_salida_obj - fecha_llegada_obj).days
            
            if noches > 0:
                precio_total = noches * cabana.precio_por_noche
        except ValueError:
            pass # Si manipulan la URL con fechas inválidas, evitamos que la app explote

    # 3. Guardar la reserva si el usuario envía el formulario (POST)
    if request.method == 'POST':
        nombre = request.POST.get('nombre_huesped')
        email = request.POST.get('email_huesped')
        telefono = request.POST.get('telefono_huesped')
        
        # OJO: Validar que tengamos fechas antes de guardar
        if fecha_llegada_obj and fecha_salida_obj:
            nueva_reserva = Reserva.objects.create(
                cabana=cabana,
                nombre_huesped=nombre,
                email_huesped=email,
                telefono_huesped=telefono,
                fecha_llegada=fecha_llegada_obj,
                fecha_salida=fecha_salida_obj,
                cantidad_personas=personas,
                precio_total=precio_total,
                estado='pendiente' # Se guarda como pendiente por defecto
            )
            # Todo salió bien, lo enviamos al home por ahora (luego podemos hacer una página de éxito)
            return redirect('reserva_exitosa', reserva_id=nueva_reserva.id)

    # 4. Mostrar el formulario (GET)
    contexto = {
        'cabana': cabana,
        'llegada': llegada_str,
        'salida': salida_str,
        'personas': personas,
        'noches': noches,
        'precio_total': precio_total,
    }
    return render(request, 'reservas/checkout.html', contexto)

def reserva_exitosa(request, reserva_id):
    # Buscamos la reserva en la base de datos
    reserva = get_object_or_404(Reserva, id=reserva_id)
    
    # Enviamos la reserva al template
    return render(request, 'reservas/exito.html', {'reserva': reserva})
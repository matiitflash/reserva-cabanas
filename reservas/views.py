from django.shortcuts import render
from .models import Cabana

def home(request):
    cabanas = Cabana.objects.all()
    
    return render(request, 'reservas/index.html', {'cabanas': cabanas})
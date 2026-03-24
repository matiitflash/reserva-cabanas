from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('buscar/', views.resultados, name='buscar'),
    path('cabana/<int:cabana_id>/', views.detalle_cabana, name='detalle_cabana'),
    path('checkout/<int:cabana_id>/', views.checkout, name='checkout'),
    path('exito/<int:reserva_id>/', views.reserva_exitosa, name='reserva_exitosa'),
]
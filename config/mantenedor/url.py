from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_principal, name='vista_principal'),
    path('agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('lista/', views.lista_clientes, name='lista_clientes'),
    path('eliminar/<int:cliente_id>/', views.eliminar_cliente, name='eliminar_cliente'),

]

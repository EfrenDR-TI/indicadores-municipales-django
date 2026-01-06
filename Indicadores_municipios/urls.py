"""
Rutas del módulo Indicadores Municipios.

Define los endpoints para la consulta y visualización
de indicadores a nivel nacional y por entidad, así como
servicios auxiliares para carga dinámica de datos.

Autor: Efrén Dolores
"""
from django.urls import path
from . import views

urlpatterns = [
    # Vista principal de indicadores (HTML)
    path('', views.mostrar_indicadores, name='mostrar_indicadores'),  # Ruta para la vista principal
    
    # Endpoint auxiliar para obtener entidades (AJAX / JSON)
    path('get_entidades/', views.get_entidades, name='get_entidades'),  # Ruta para obtener las entidades
]

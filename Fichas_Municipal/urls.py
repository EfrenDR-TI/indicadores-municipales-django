"""
URL configuration for Fichas_Municipal project.

Define las rutas principales del sistema para la visualización
y gestión de indicadores municipales, así como herramientas
de carga de datos y administración.

Autor: Efrén Dolores
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Panel administrativo de Django
    path('admin/', admin.site.urls),

     # Rutas principales del módulo de indicadores municipales
    path('', include('Indicadores_municipios.urls')),  # Esta línea es suficiente
    
    # Módulo Data Wizard para carga y gestión de datasets
    path('datawizard/', include('data_wizard.urls')),
    
]


"""
Vistas principales para la consulta y visualización de indicadores.

Este módulo gestiona la obtención, filtrado y preparación de datos
a nivel nacional y por entidad, para su representación en mapas
y gráficas interactivas.

Autor: Efrén Dolores
"""

from django.shortcuts import render
from django.http import JsonResponse
from .models import Table_indicadores
from .functions import (
    obtener_datos_mapa,
    obtener_datos_entidad,
    obtener_datos_nacional,
    obtener_datos_grafica
)
import logging

logger = logging.getLogger(__name__)

# ------------------------------------------------------------------
# Vista principal de indicadores
# ------------------------------------------------------------------
def mostrar_indicadores(request):
    """
    Vista principal del sistema de indicadores.

    Permite consultar indicadores a nivel nacional o por entidad,
    procesando los datos necesarios para tablas, mapas y gráficas
    a partir de los parámetros recibidos vía GET.
    """
    # Parámetros de entrada
    nivel = request.GET.get('nivel', 'nacional')  
    indicador = request.GET.get('indicador', None)  
    entidad = request.GET.get('entidad', None)

    # Catálogo de indicadores disponibles por nivel de análisis
    indicadores_disponibles = {
         'nacional': [
            # Indicadores agregados a nivel nacional
             {'value': 'Porc_ind_N', 'label': 'Porcentaje de población indígena '}, 
             {'value': 'Porc_no_ind_N', 'label': 'Porcentaje de población no indígena '},
             {'value': 'Porc_hli_3mas_N', 'label': 'Porcentaje de hablantes de lengua indígena de 3 años y más '},
             {'value': 'Porc_no_hli_N', 'label': 'Porcentaje de no hablantes de lengua indígena de 3 años y más'},
             {'value': 'Porc_ne_hli_N', 'label': 'Porcentaje de condición hablante de lengua indígena de 3 años y más no especificada'},
             {'value': 'Porc_hli_3mas_espa_N', 'label': 'Porcentaje de hablantes de lengua indígena y de español de 3 años y más'},
             {'value': 'Porc_hli_3mas_Noespa_N', 'label': 'Porcentaje de hablantes de lengua indígena monolingües'},
             {'value': 'PorcC_hli_3mas_NE_N', 'label': 'Porcentaje de condición hablante de español de 3 años y más no especificada'},
             {'value': 'Porc_hli_3A5_N', 'label': 'Porcentaje hablante de lengua indígena de 3 a 5 años'},
             {'value': 'Porc_hli_6A11_N', 'label': 'Porcentaje hablante de lengua indígena de 6 a 11 años'},
             {'value': 'Porc_hli_12A14_N', 'label': 'Porcentaje hablante de lengua indígena de 12 a 14 años'},
             {'value': 'Porc_hli_15A17_N', 'label': 'Porcentaje hablante de lengua indígena de 15 a 17 años'},
             {'value': 'Porc_analfa_t_N', 'label': 'Porcentaje analfabetismo 15 años total '},
             {'value': 'Porc_analfa_h_N', 'label': ' Porcentaje analfabetismo 15 años y más por hombre'},
             {'value': 'Porc_analfa_m_N', 'label': 'Porcentaje analfabetismo 15 años y más por mujer '},
             {'value': 'Porc_aleb_20A24_N', 'label': 'Porcentaje de 20 a 24 con educación básica '},
             {'value': 'Porc_alems_20A24_N', 'label': 'Porcentaje de 20 a 24 con EMS '},
             {'value': 'Tasa_asis_3a5_N', 'label': 'Tasa asistencia grupo 3 a 5 '},
             {'value': 'Tasa_asis_6a11_N', 'label': 'Tasa asistencia grupo 6 a 11 '},
             {'value': 'Tasa_asis_12a14_N', 'label': 'Tasa asistencia grupo 12 a 14 '},
             {'value': 'Tasa_asis_15a17_N', 'label': 'Tasa asistencia grupo 15 a 17 '},
             {'value': 'Gpr_inegi_H_N', 'label': 'Grado promedio de escolaridad por hombres '},
             {'value': 'Gpr_inegi_M_N', 'label': 'Grado promedio de escolaridad por mujeres '},
             {'value': 'Gpr_Inegi_T_N', 'label': 'Grado promedio de escolaridad total '}

        ],
        'entidad': [
            # Indicadores agregados a nivel entidad
            {'value': 'Porc_ind', 'label': 'Porcentaje de población indígena'},
            {'value': 'Porc_no_ind', 'label': 'Porcentaje de población no indígena'},
            {'value': 'Porc_hli_3mas', 'label': 'Porcentaje de hablantes de lengua indígena de 3 años y más'},
            {'value': 'Porc_no_hli', 'label': 'Porcentaje de no hablantes de lengua indígena de 3 años y más'},
            {'value': 'Porc_ne_hli', 'label': 'Porcentaje de condición hablante de lengua indígena de 3 años y más no especificada'},
            {'value': 'Porc_hli_3mas_espa', 'label': 'Porcentaje de hablantes de lengua indígena y de español de 3 años y más'},
            {'value': 'Porc_hli_3mas_Noespa', 'label': 'Porcentaje de hablantes de lengua indígena monolingües'},
            {'value': 'PorcC_hli_3mas_NE', 'label': 'Porcentaje de condición hablante de español de 3 años y más no especificada'},
            {'value': 'Porc_hli_3A5', 'label': 'Porcentaje hablante de lengua indígena de 3 a 5 años'},
            {'value': 'Porc_hli_6A11', 'label': 'Porcentaje hablante de lengua indígena de 6 a 11 años'},
            {'value': 'Porc_hli_12A14', 'label': 'Porcentaje hablante de lengua indígena de 12 a 14 años'},
            {'value': 'Porc_hli_15A17', 'label': 'Porcentaje hablante de lengua indígena de 15 a 17 años'},
            {'value': 'Porc_analfa_t', 'label': 'Porcentaje analfabetismo 15 años total '},
            {'value': 'Porc_analfa_h', 'label': 'Porcentaje analfabetismo 15 años y más por hombre'},
            {'value': 'Porc_analfa_m', 'label': 'Porcentaje analfabetismo 15 años y más por mujer'},
            {'value': 'Porc_aleb_20A24', 'label': 'Porcentaje de 20 a 24 con educación básica'},
            {'value': 'Porc_alems_20A24', 'label': 'Porcentaje de 20 a 24 con EMS'},
            {'value': 'Tasa_asis_3a', 'label': 'Tasa asistencia grupo 3 a 5'},
            {'value': 'Tasa_asis_6a11', 'label': 'Tasa asistencia grupo 6 a 11'},
            {'value': 'Tasa_asis_12a14', 'label': 'Tasa asistencia grupo 12 a 14'},
            {'value': 'Tasa_asis_15a17', 'label': 'Tasa asistencia grupo 15 a 17'},
            {'value': 'Gpr_inegi_H', 'label': 'Grado promedio de escolaridad por hombres'},
            {'value': 'Gpr_inegi_M', 'label': 'Grado promedio de escolaridad por mujeres'},
            {'value': 'Gpr_Inegi_T', 'label': 'Grado promedio de escolaridad total'},

        ]
    }

    indicadores = indicadores_disponibles.get(nivel, [])

    # Obtención de la etiqueta descriptiva del indicador seleccionado                              
    indicador_label = ""                                                           
    if indicador:                                                                  
        for etiqueta in indicadores:                                               
            if etiqueta['value'] == indicador:                                            
                indicador_label = etiqueta['label']                                
                break                                                                      

    # Inicializa de contenedores de datos
    datos = []
    datos_mapa = []
    datos_grafica = []

    # Procesamiento de datos según nivel de análisis
    try:
        if indicador:
            if nivel == 'nacional':
                datos = obtener_datos_nacional(indicador)
                datos_mapa = obtener_datos_mapa(indicador, nivel)
                datos_grafica = obtener_datos_grafica(indicador, nivel)
                logger.info(f"Datos nacionales obtenidos: {datos_grafica}")
            
            elif nivel == 'entidad' and entidad:
                datos = obtener_datos_entidad(indicador, entidad)
                datos_mapa = obtener_datos_mapa(indicador, nivel, entidad)
                datos_grafica = obtener_datos_grafica(indicador, nivel, entidad)
                logger.info(f"Datos entidad obtenidos: {datos_grafica}")
    except Exception as e:
        logger.error(f"Error al procesar datos: {e}")

    # Renderizado de la vista principal
    return render(request, 'Indicadores_municipios.html', {
        'datos': datos,
        'datos_mapa': datos_mapa,
        'datos_grafica': datos_grafica,
        'nivel': nivel,
        'indicador': indicador,
        'indicador_seleccionado': indicador,
        'indicador_label': indicador_label, 
        'indicadores_disponibles': indicadores,
        'entidades': Table_indicadores.objects.values_list('NOM_ENT', flat=True).distinct(),
        'entidad_seleccionada': entidad,
        'entidad': entidad,
    })

# ------------------------------------------------------------------
# Vista auxiliar para obtención de entidades (AJAX)
# ------------------------------------------------------------------
def get_entidades(request):
    """
    Devuelve el listado de entidades federativas disponibles.

    Utilizada principalmente para cargas dinámicas
    en el nivel de análisis por entidad.
    """
    nivel = request.GET.get('nivel', '')
    if nivel == 'entidad': 
        entidades = Table_indicadores.objects.values('NOM_ENT').distinct()
        data = [{'NOM_ENT': entidad['NOM_ENT']} for entidad in entidades]
    else:
        data = []  

    return JsonResponse(data, safe=False)


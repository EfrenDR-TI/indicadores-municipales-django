"""
Formularios para la selección y validación de filtros de indicadores.

Este módulo centraliza la validación de parámetros utilizados
en la consulta de indicadores a nivel nacional y por entidad,
asegurando coherencia entre nivel de análisis e inputs del usuario.

Autor: Efrén Dolores
"""

from django import forms
from .models import Table_indicadores

class FiltroForm(forms.Form):
    """
    Formulario de filtros para la consulta de indicadores.

    Permite seleccionar el nivel de análisis, la entidad
    (cuando aplica) y el indicador a visualizar.
    """

    NIVEL_CHOICES = [
        ('nacional', 'Nivel Nacional'),
        ('entidad', 'Por Entidad'),
    ]

    """
        Obtiene dinámicamente el listado de entidades disponibles
        a partir de la base de datos.
        """
    def obtener_entidades():
        return [(entidad, entidad) for entidad in Table_indicadores.objects.values_list('NOM_ENT', flat=True).distinct()]

    nivel = forms.ChoiceField(
        choices=NIVEL_CHOICES, 
        label="Seleccionar por nivel nacional o por entidad", 
        required=True
    )

    entidad = forms.ChoiceField(
        choices=[],
        label="Seleccionar Entidad",
        required=False,  # Cambia a obligatorio si nivel es "entidad"
    )

    indicador = forms.ChoiceField(
        choices=[('Porc_ind', 'Porcentaje de Población Indígena'),
                 ('Porc_no_ind', 'Porcentaje de Población no Indígena'),
                 ('Porc_hli_3mas', 'Porcentaje de hablantes de lengua indígena de 3 años y más'),
                 ('Porc_no_hli', 'Porcentaje de no hablantes de lengua indígena de 3 años y más'),
                 ('Porc_ne_hli', 'Porcentaje de condición hablante de lengua indígena de 3 años y más no especificada por entidad'),
                 ('Porc_hli_3mas_espa', 'Porcentaje de hablantes de lengua indígena y de español de 3 años y más por entidad'),
                 ('Porc_hli_3mas_Noespa', 'Porcentaje de hablantes de lengua indígena monolingües'),
                 ('PorcC_hli_3mas_NE', 'Porcentaje de condición hablante de español de 3 años y más no especificada'),
                 ('Porc_hli_3A5', 'Porcentaje hablante de lengua indígena de 3 a 5 años'),
                 ('Porc_hli_6A11', 'Porcentaje hablante de lengua indígena de 6 a 11 años'),
                 ('Porc_hli_12A14', 'Porcentaje hablante de lengua indígena de 12 a 14 años'),
                 ('Porc_hli_15A17', 'Porcentaje hablante de lengua indígena de 15 a 17 años'),
                 ('Porc_analfa_t', 'Porcentaje analfabetismo 15 años y más por entidad'),
                 ('Porc_analfa_h', 'Porcentaje analfabetismo 15 años y más, hombres por entidad'),
                 ('Porc_analfa_m', 'Porcentaje analfabetismo 15 años y más, mujeres por entidad'),
                 ('Porc_aleb_20A24', 'Porcentaje de 20 a 24 con educación básica por entidad'),
                 ('Porc_alems_20A24', 'Porcentaje de 20 a 24 con EMS'),
                 ('Tasa_asis_3a5', 'Tasa asistencia grupo 3 a 5'),
                 ('Tasa_asis_6a11', 'Tasa asistencia grupo 6 a 11'),
                 ('Tasa_asis_12a14', 'Tasa asistencia grupo 12 a 14'),
                 ('Tasa_asis_15a17', 'Tasa asistencia grupo 15 a 17'),
                 ('Gpr_inegi_H', 'Grado promedio de escolaridad hombres'),
                 ('Gpr_inegi_M', 'Grado promedio de escolaridad mujeres'),
                 ('Gpr_Inegi_T', 'Grado promedio de escolaridad')],
        label="Seleccionar por Indicador",
        required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Actualizar dinámicamente las opciones de 'entidad'
        self.fields['entidad'].choices = self.obtener_entidades()

    def clean(self):
        """
        Validación cruzada de campos.

        Obliga a seleccionar entidad cuando el nivel
        de análisis es por entidad.
        """
        cleaned_data = super().clean()
        nivel = cleaned_data.get('nivel')
        entidad = cleaned_data.get('entidad')

        if nivel == 'entidad' and not entidad:
            self.add_error('entidad', 'Debe seleccionar una entidad si el nivel es "Por Entidad".')

        return cleaned_data

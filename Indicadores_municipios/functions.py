# functions.py
from .models import Table_indicadores, Table_indicadores_Entidad
from django.db.models import F, Value, CharField
from django.db.models.functions import Concat ,Round

#########################################################################################################
################## Función para obtener datos simplificados para el mapa ################################
def obtener_datos_mapa(indicador, nivel, entidad=None):

    # Mapea códigos de entidades a las claves de Highcharts
    clave_mapa = {
        "01": "mx-ag",   # Aguascalientes
        "02": "mx-bc",    # Baja California
        "03": "mx-bs",    # Baja California Sur
        "04": "mx-cm",    # Campeche
        "05": "mx-co",    # Coahuila
        "06": "mx-cl",    # Colima
        "07": "mx-cs",    # Chiapas
        "08": "mx-ch",    # Chihuahua
        "09": "mx-df",    # Ciudad de México
        "10": "mx-dg",    # Durango
        "11": "mx-gj",    # Guanajuato
        "12": "mx-gr",    # Guerrero
        "13": "mx-hg",    # Hidalgo
        "14": "mx-ja",    # Jalisco
        "15": "mx-mx",    # Estado de México
        "16": "mx-mi",    # Michoacán
        "17": "mx-mo",    # Morelos
        "18": "mx-na",    # Nayarit
        "19": "mx-nl",    # Nuevo León
        "20": "mx-oa",    # Oaxaca
        "21": "mx-pu",    # Puebla
        "22": "mx-qt",    # Querétaro
        "23": "mx-qr",    # Quintana Roo
        "24": "mx-sl",    # San Luis Potosí
        "25": "mx-si",    # Sinaloa
        "26": "mx-so",    # Sonora
        "27": "mx-tb",    # Tabasco
        "28": "mx-tm",    # Tamaulipas
        "29": "mx-tl",    # Tlaxcala
        "30": "mx-ve",    # Veracruz
        "31": "mx-yu",    # Yucatán
        "32": "mx-za"     # Zacatecas
    }
 
    if nivel =='nacional':
   
        # Define las columnas según los indicadores
        columna = {

            "Porc_ind_N": "PORC_IND_ENT",        # Porcentaje de población indígena
            "Porc_no_ind_N": "PORC_NO_IND_ENT",  # Porcentaje de población no indígena
            "Porc_hli_3mas_N": "porc_hli_3mas_ENT",
            "Porc_no_hli_N": "porc_no_hli_ENT", 
            "Porc_ne_hli_N": "porc_ne_hli_ENT",  
            "Porc_hli_3mas_espa_N": "porc_hli_3mas_espa_ENT",
            "Porc_hli_3mas_Noespa_N": "porc_hii_3mas_Noespa_ENT",
            "PorcC_hli_3mas_NE_N": "Porc_hli_3mas_NE_ENT",
            "Porc_hli_3A5_N": "PORC_HLI_3A5_ENT",        
            "Porc_hli_6A11_N": "PORC_HLI_6A11_ENT",
            "Porc_hli_12A14_N": "PORC_HLI_12A14_ENT",
            "Porc_hli_15A17_N": "PORC_HLI_15A17_ENT",
            "Porc_analfa_t_N": "PORC_ANALFA_T_ENT",
            "Porc_analfa_h_N": "PORC_ANALFA_H_ENT",
            "Porc_analfa_m_N": "PORC_ANALFA_M_ENT",
            "Porc_aleb_20A24_N": "PORC_ALEB_20A24_ENT",
            "Porc_alems_20A24_N": "PORC_ALEMS_20A24_ENT",
            "Tasa_asis_3a5_N": "tasa_asis_3a5_ent",
            "Tasa_asis_6a11_N": "tasa_asis_6a11_ent",
            "Tasa_asis_12a14_N": "tasa_asis_12a14_ent",
            "Tasa_asis_15a17_N": "tasa_asis_15a17_ent",
            "Gpr_inegi_H_N": "GPR_INEGI_H_ENT",
            "Gpr_inegi_M_N": "GPR_INEGI_M_ENT",
            "Gpr_inegi_T_N": "GPR_INEGI_T_ENT",    

        # Agrega más indicadores si es necesario
        }.get(indicador)
        if not columna:
            return []
   
        datos = Table_indicadores_Entidad.objects.values(
                hc_key=F("CVE_ENT"),  # Clave compatible con Highcharts
                value=Round(F(columna),2)      # Valor asociado al indicador
            )
            # Mapea las claves al formato esperado por Highcharts

        datos_mapa = [
                {"hc_key": clave_mapa.get(item["hc_key"], ""), "value": item["value"]}
                for item in datos if item["hc_key"] in clave_mapa
        ]
        return datos_mapa
    
    elif nivel == 'entidad' and entidad:
        # Mapea columnas según indicadores
        columna_m = {
            "Porc_ind": "PORC_IND",
            "Porc_no_ind": "PORC_NO_IND",
            "Porc_hli_3mas": "PORC_HLI_3mas",
            "Porc_no_hli": "PORC_NO_HLI",
            "Porc_ne_hli": "PORC_NE_HLI",
            "Porc_hli_3mas_espa": "PORC_HLI_3mas_espa",
            "Porc_hli_3mas_Noespa": "PORC_HLI_3mas_Noespa",
            "PorcC_hli_3mas_NE": "PORC_HLI_3mas_NE",
            "Porc_hli_3A5": "PORC_HLI_3A5",
            "Porc_hli_6A11": "PORC_HLI_6A11",
            "Porc_hli_12A14": "PORC_HLI_12A14",
            "Porc_hli_15A17": "PORC_HLI_15A17",
            "Porc_analfa_t": "PORC_ANALFA_T",
            "Porc_analfa_h": "PORC_ANALFA_H",
            "Porc_analfa_m": "PORC_ANALFA_M",
            "Porc_aleb_20A24": "PORC_ALEB_20A24",
            "Porc_alems_20A24": "PORC_ALEMS_20A24",
            "Tasa_asis_3a5": "tasa_asis_3a5",
            "Tasa_asis_6a11": "tasa_asis_6a11",
            "Tasa_asis_12a14": "tasa_asis_12a14",
            "Tasa_asis_15a17": "tasa_asis_15a17",
            "Gpr_inegi_H": "GPR_Inegi_H",
            "Gpr_inegi_M": "GPR_Inegi_M",
            "Gpr_Inegi_T": "GPR_Inegi_T"
            
            # Agrega más indicadores según sea necesario
        }.get(indicador)

        if not columna_m:
            return []  # Si no se encuentra el indicador, retorna una lista vacía
        # Relación NOM_ENT -> CVE_ENT (sta_code)
        nom_ent_to_sta_code = {
            "Aguascalientes": "01",
            "Baja California": "02",
            "Baja California Sur": "03",
            "Campeche": "04",
            "Coahuila de Zaragoza": "05",
            "Colima": "06",
            "Chiapas": "07",
            "Chihuahua": "08",
            "Ciudad de México": "09",
            "Durango": "10",
            "Guanajuato": "11",
            "Guerrero": "12",
            "Hidalgo": "13",
            "Jalisco": "14",
            "México": "15",
            "Michoacán de Ocampo": "16",
            "Morelos": "17",
            "Nayarit": "18",
            "Nuevo León": "19",
            "Oaxaca": "20",
            "Puebla": "21",
            "Querétaro": "22",
            "Quintana Roo": "23",
            "San Luis Potosí": "24",
            "Sinaloa": "25",
            "Sonora": "26",
            "Tabasco": "27",
            "Tamaulipas": "28",
            "Tlaxcala": "29",
            "Veracruz": "30",
            "Yucatán": "31",
            "Zacatecas": "32"
        }         
        # Obtén el código de la entidad (CVE_ENT) basado en el nombre
        entidad_prefijo = nom_ent_to_sta_code.get(entidad)
        if not entidad_prefijo:
            return []  # Si no se encuentra la entidad, retorna una lista vacía

        # Filtra los datos desde el modelo
        datos = Table_indicadores.objects.filter(
            CVE_ENT=entidad_prefijo
        ).values(
            mun_code=F("CLAVE"),  # Clave del municipio
            name=F("NOM_MUN"),  # Nombre del municipio
            value=Round(F(columna_m),2)  # Valor del indicador
        )

        # Prepara los datos en el formato esperado por Highcharts
        datos_mapa = [
                {
                    "mun_code": item["mun_code"],   # Usa la clave como identificador
                    "name": item["name"],      # Nombre del municipio
                    "value": item["value"]     # Valor del indicador
                }
                for item in datos
            ]
        return datos_mapa
         # return list(datos)  # Devuelve los datos como lista
        #return []  # Si el indicador no es válido, devuelve lista vacía

#################################################################################################
############ Función para obtener datos para la grafica nivel entidad ###########################
def obtener_datos_grafica(indicador, nivel, entidad=None):
    if nivel == 'nacional':
        # Diccionario que mapea indicadores a sus columnas correspondientes en el modelo
        columna = {
            "Porc_ind_N": "PORC_IND_ENT",        # Porcentaje de población indígena 
            "Porc_no_ind_N": "PORC_NO_IND_ENT",  # Porcentaje de población no indígena
            "Porc_hli_3mas_N": "porc_hli_3mas_ENT",
            "Porc_no_hli_N": "porc_no_hli_ENT", 
            "Porc_ne_hli_N": "porc_ne_hli_ENT",  
            "Porc_hli_3mas_espa_N": "porc_hli_3mas_espa_ENT",
            "Porc_hli_3mas_Noespa_N": "porc_hii_3mas_Noespa_ENT",
            "PorcC_hli_3mas_NE_N": "Porc_hli_3mas_NE_ENT",
            "Porc_hli_3A5_N": "PORC_HLI_3A5_ENT",        
            "Porc_hli_6A11_N": "PORC_HLI_6A11_ENT",
            "Porc_hli_12A14_N": "PORC_HLI_12A14_ENT",
            "Porc_hli_15A17_N": "PORC_HLI_15A17_ENT",
            "Porc_analfa_t_N": "PORC_ANALFA_T_ENT",
            "Porc_analfa_h_N": "PORC_ANALFA_H_ENT",
            "Porc_analfa_m_N": "PORC_ANALFA_M_ENT",
            "Porc_aleb_20A24_N": "PORC_ALEB_20A24_ENT",
            "Porc_alems_20A24_N": "PORC_ALEMS_20A24_ENT",
            "Tasa_asis_3a5_N": "tasa_asis_3a5_ent",
            "Tasa_asis_6a11_N": "tasa_asis_6a11_ent",
            "Tasa_asis_12a14_N": "tasa_asis_12a14_ent",
            "Tasa_asis_15a17_N": "tasa_asis_15a17_ent",
            "Gpr_inegi_H_N": "GPR_INEGI_H_ENT",
            "Gpr_inegi_M_N": "GPR_INEGI_M_ENT",
            "Gpr_inegi_T_N": "GPR_INEGI_T_ENT", 
            # Agrega más indicadores según sea necesario
        }.get(indicador)

        if not columna:
            return []

        # Consulta a la base de datos obteniendo los valores para el indicador especificado
        datos = Table_indicadores_Entidad.objects.values(
            categoria=F("NOM_ENT"),  # Nombre de la entidad como categoría
            valor=Round(F(columna), 2)  # Valor del indicador, redondeado a 2 decimales
        )
        # Formatear los datos para Highcharts
        datos_grafica = [
            {"name": item["categoria"], "y": item["valor"]}
            for item in datos
        ]
        return datos_grafica
    
    elif nivel == 'entidad' and entidad:
        # Validar que la entidad exista y obtener su código
        entidad_codigo = Table_indicadores.objects.filter(
            NOM_ENT=entidad
        ).values_list('CVE_ENT', flat=True).first()

        if not entidad_codigo:
            logger.warning(f"No se encontró un código válido para la entidad '{entidad}'.")
            return []

        # Mapea indicadores a columnas correspondientes en el modelo
        columna_m = {
            "Porc_ind": "PORC_IND",
            "Porc_no_ind": "PORC_NO_IND",
            "Porc_hli_3mas": "PORC_HLI_3mas",
            "Porc_no_hli": "PORC_NO_HLI",
            "Porc_ne_hli": "PORC_NE_HLI",
            "Porc_hli_3mas_espa": "PORC_HLI_3mas_espa",
            "Porc_hli_3mas_Noespa": "PORC_HLI_3mas_Noespa",
            "PorcC_hli_3mas_NE": "PORC_HLI_3mas_NE",
            "Porc_hli_3A5": "PORC_HLI_3A5",
            "Porc_hli_6A11": "PORC_HLI_6A11",
            "Porc_hli_12A14": "PORC_HLI_12A14",
            "Porc_hli_15A17": "PORC_HLI_15A17",
            "Porc_analfa_t": "PORC_ANALFA_T",
            "Porc_analfa_h": "PORC_ANALFA_H",
            "Porc_analfa_m": "PORC_ANALFA_M",
            "Porc_aleb_20A24": "PORC_ALEB_20A24",
            "Porc_alems_20A24": "PORC_ALEMS_20A24",
            "Tasa_asis_3a5": "tasa_asis_3a5",
            "Tasa_asis_6a11": "tasa_asis_6a11",
            "Tasa_asis_12a14": "tasa_asis_12a14",
            "Tasa_asis_15a17": "tasa_asis_15a17",
            "Gpr_inegi_H": "GPR_Inegi_H",
            "Gpr_inegi_M": "GPR_Inegi_M",
            "Gpr_Inegi_T": "GPR_Inegi_T"
            # Agrega más indicadores según sea necesario
        }.get(indicador)

        if not columna_m:
            logger.warning(f"Indicador '{indicador}' no tiene un mapeo válido.")
            return []

        # Consulta a la base de datos filtrando por la entidad
        datos = Table_indicadores.objects.filter(
            CVE_ENT=entidad_codigo
        ).values(
            categoria=F("NOM_MUN"),  # Nombre del municipio como categoría
            valor=Round(F(columna_m), 2)  # Valor del indicador, redondeado a 2 decimales
        )

        # Validar si la consulta retorna datos
        if not datos.exists():
            logger.warning(f"No se encontraron datos para la entidad '{entidad_codigo}' y el indicador '{columna_m}'.")
            return []

        # Formatear los datos para Highcharts
        datos_grafica = [
            {"name": item["categoria"], "y": item["valor"]}
            for item in datos
        ]
        return datos_grafica

    return []

###################################################################################################
################### Función para obtener datos a nivel nacional ###################################
def obtener_datos_nacional(indicador):
    if indicador == 'Porc_ind_N': ##1
        # Consulta y renombra columnas para el indicador 'Porc_ind'
        datos = (
            Table_indicadores_Entidad.objects.annotate(
                Clave_de_la_entidad=F('CVE_ENT'),
                Nombre_de_la_entidad=F('NOM_ENT'),
                Población_indígena=F('INDIGENA_ENT'),
                Población_total=F('POB_TOTAL_ENT'),
                
                Porcentaje_de_población_indígena=Concat(Round(F('PORC_IND_ENT'),2), Value(' %'), output_field=CharField())
            )
            .values(
                'Clave_de_la_entidad',
                'Nombre_de_la_entidad',
                'Población_indígena',
                'Población_total',
                'Porcentaje_de_población_indígena',
            )
        )
    elif indicador == 'Porc_no_ind_N': ##2
        # Consulta y renombra columnas para el indicador 'Porc_no_ind'
        datos = (
            Table_indicadores_Entidad.objects.annotate(
                Clave_de_la_entidad=F('CVE_ENT'),
                Nombre_de_la_entidad=F('NOM_ENT'),
                Población_no_indígena=F('NO_IND_ENT'),
                Población_total=F('POB_TOTAL_ENT'),
                Porcentaje_de_población_no_indígena=Concat(Round(F('PORC_NO_IND_ENT'),2), Value(' %'), output_field=CharField())
            )
            .values(
                'Clave_de_la_entidad',
                'Nombre_de_la_entidad',
                'Población_no_indígena',
                'Población_total',
                'Porcentaje_de_población_no_indígena',
            )
        )        
    elif indicador == 'Porc_hli_3mas_N': ##3
        # Consulta y renombra columnas para el indicador 'Porc_hli_3mas'
        datos = (
            Table_indicadores_Entidad.objects.annotate(
                Clave_de_la_entidad=F('CVE_ENT'),
                Nombre_de_la_entidad=F('NOM_ENT'),
                Hablantes_de_lengua_indígena_de_3_años_y_más=F('HLI_3YMAS_ENT'),
                Población_de_3_y_más_años=F('POB3YMAS_ENT'),
                Porcentaje_de_hablantes_de_lengua_indígena_de_3_años_y_más=Concat(Round(F('porc_hli_3mas_ENT'),2), Value(' %'), output_field=CharField())
            )
            .values(
                'Clave_de_la_entidad',
                'Nombre_de_la_entidad',
                'Hablantes_de_lengua_indígena_de_3_años_y_más',
                'Población_de_3_y_más_años',
                'Porcentaje_de_hablantes_de_lengua_indígena_de_3_años_y_más',
            )
        )
    elif indicador == 'Porc_no_hli_N': ##4
        # Consulta y renombra columnas para el indicador 'Porc_hli_3mas'
        datos = (
            Table_indicadores_Entidad.objects.annotate(
                Clave_de_la_entidad=F('CVE_ENT'),
                Nombre_de_la_entidad=F('NOM_ENT'),
                No_hablantes_de_lengua_indígena_de_3_años_y_más=F('NO_HLI_ENT'),
                Población_de_3_y_más_años=F('POB3YMAS_ENT'),
                Porcentaje_de_no_hablantes_de_lengua_indígena_de_3_años_y_más=Concat(Round(F('porc_no_hli_ENT'),2),Value(' %'), output_field=CharField())
            )
            .values(
                'Clave_de_la_entidad',
                'Nombre_de_la_entidad',
                'No_hablantes_de_lengua_indígena_de_3_años_y_más',
                'Población_de_3_y_más_años',
                'Porcentaje_de_no_hablantes_de_lengua_indígena_de_3_años_y_más',
            )
        )
    elif indicador == 'Porc_ne_hli_N': ##5
        # Consulta y renombra columnas para el indicador 'Porc_hli_3mas'
        datos = (
            Table_indicadores_Entidad.objects.annotate(
                Clave_de_la_entidad=F('CVE_ENT'),
                Nombre_de_la_entidad=F('NOM_ENT'),
                Condición_hablante_de_lengua_indígena_de_3_años_y_más_no_especificada=F('NE_HLI_ENT'),
                Población_de_3_y_más_años=F('POB3YMAS_ENT'),
                Porcentaje_de_condición_hablante_de_lengua_indígena_de_3_años_y_más_no_especificada=Concat(Round(F('porc_ne_hli_ENT'),2),Value(' %'), output_field=CharField())
            )
            .values(
                'Clave_de_la_entidad',
                'Nombre_de_la_entidad',
                'Condición_hablante_de_lengua_indígena_de_3_años_y_más_no_especificada',
                'Población_de_3_y_más_años',
                'Porcentaje_de_condición_hablante_de_lengua_indígena_de_3_años_y_más_no_especificada',
            )
        )
    elif indicador == 'Porc_hli_3mas_espa_N': ##6
        # Consulta y renombra columnas para el indicador 'Porc_hli_3mas'
        datos = (
            Table_indicadores_Entidad.objects.annotate(
                Clave_de_la_entidad=F('CVE_ENT'),
                Nombre_de_la_entidad=F('NOM_ENT'),
                Hablantes_de_lengua_indígena_y_de_español_de_3_años_y_más=F('HLI_3mas_espa_ENT'),
                Hablantes_de_lengua_indígena_de_3_años_y_más=F('HLI_3YMAS_ENT'),
                Porcentaje_de_hablantes_de_lengua_indígena_y_de_español_de_3_años_y_más=Concat(Round(F('porc_hli_3mas_espa_ENT'),2),Value(' %'), output_field=CharField())
            )
            .values(
                'Clave_de_la_entidad',
                'Nombre_de_la_entidad',
                'Hablantes_de_lengua_indígena_y_de_español_de_3_años_y_más',
                'Hablantes_de_lengua_indígena_de_3_años_y_más',
                'Porcentaje_de_hablantes_de_lengua_indígena_y_de_español_de_3_años_y_más',
            )
        )
    elif indicador == 'Porc_hli_3mas_Noespa_N': ##7
        # Consulta y renombra columnas para el indicador 'Porc_hli_3mas'
        datos = (
            Table_indicadores_Entidad.objects.annotate(
                Clave_de_la_entidad=F('CVE_ENT'),
                Nombre_de_la_entidad=F('NOM_ENT'),
                Hablantes_de_lengua_indígena_monolingües=F('HLI_3mas_Noespa_ENT'),
                Hablantes_de_lengua_indígena_de_3_años_y_más=F('HLI_3YMAS_ENT'),
                Porcentaje_de_hablantes_de_lengua_indígena_monolingües=Concat(Round(F('porc_hii_3mas_Noespa_ENT'),2),Value(' %'), output_field=CharField())
            )
            .values(
                'Clave_de_la_entidad',
                'Nombre_de_la_entidad',
                'Hablantes_de_lengua_indígena_monolingües',
                'Hablantes_de_lengua_indígena_de_3_años_y_más',
                'Porcentaje_de_hablantes_de_lengua_indígena_monolingües',
            )
        )
    elif indicador == 'PorcC_hli_3mas_NE_N': ##8
        # Consulta y renombra columnas para el indicador 'Porc_hli_3mas'
        datos = (
            Table_indicadores_Entidad.objects.annotate(
                Clave_de_la_entidad=F('CVE_ENT'),
                Nombre_de_la_entidad=F('NOM_ENT'),
                Condición_hablante_de_español_de_3_años_y_más_no_especificada=F('HLI_3mas_NE_ENT'),
                Hablantes_de_lengua_indígena_de_3_años_y_más=F('HLI_3YMAS_ENT'),
                Porcentaje_de_condición_hablante_de_español_de_3_años_y_más_no_especificada=Concat(Round(F('Porc_hli_3mas_NE_ENT'),2),Value(' %'), output_field=CharField())
            )
            .values(
                'Clave_de_la_entidad',
                'Nombre_de_la_entidad',
                'Condición_hablante_de_español_de_3_años_y_más_no_especificada',
                'Hablantes_de_lengua_indígena_de_3_años_y_más',
                'Porcentaje_de_condición_hablante_de_español_de_3_años_y_más_no_especificada',
            )
        )
    elif indicador == 'Porc_hli_3A5_N': ##9
        # Consulta y renombra columnas para el indicador 'Porc_hli_3mas'
        datos = (
            Table_indicadores_Entidad.objects.annotate(
                Clave_de_la_entidad=F('CVE_ENT'),
                Nombre_de_la_entidad=F('NOM_ENT'),
                Población_hablante_de_lengua_indígena_de_3_a_5_años=F('HLI_3A5_ENT'),
                Población_de_3_a_5_años=F('POB_3A5_ENT'),
                Porcentaje_hablante_de_lengua_indígena_de_3_a_5_años=Concat(Round(F('PORC_HLI_3A5_ENT'),2),Value(' %'), output_field=CharField())
            )
            .values(
                'Clave_de_la_entidad',
                'Nombre_de_la_entidad',
                'Población_hablante_de_lengua_indígena_de_3_a_5_años',
                'Población_de_3_a_5_años',
                'Porcentaje_hablante_de_lengua_indígena_de_3_a_5_años',
            )
        )
    elif indicador == 'Porc_hli_6A11_N': ##10
        # Consulta y renombra columnas para el indicador 'Porc_hli_3mas'
        datos = (
            Table_indicadores_Entidad.objects.annotate(
                Clave_de_la_entidad=F('CVE_ENT'),
                Nombre_de_la_entidad=F('NOM_ENT'),
                Población_hablante_de_lengua_indígena_de_6_a_11_años=F('HLI_6A11_ENT'),
                Población_de_6_a_11_años=F('POB_6A11_ENT'),
                Porcentaje_hablante_de_lengua_indígena_de_6_a_11_años=Concat(Round(F('PORC_HLI_6A11_ENT'),2),Value(' %'), output_field=CharField())
            )
            .values(
                'Clave_de_la_entidad',
                'Nombre_de_la_entidad',
                'Población_hablante_de_lengua_indígena_de_6_a_11_años',
                'Población_de_6_a_11_años',
                'Porcentaje_hablante_de_lengua_indígena_de_6_a_11_años',
            )
        )
    elif indicador == 'Porc_hli_12A14_N': ##11
        # Consulta y renombra columnas para el indicador 'Porc_hli_3mas'
        datos = (
            Table_indicadores_Entidad.objects.annotate(
                Clave_de_la_entidad=F('CVE_ENT'),
                Nombre_de_la_entidad=F('NOM_ENT'),
                Población_hablante_de_lengua_indígena_de_12_a_14_años=F('HLI_12A14_ENT'),
                Población_de_12_a_14_años=F('POB_12A14_ENT'),
                Porcentaje_hablante_de_lengua_indígena_de_12_a_14_años=Concat(Round(F('PORC_HLI_12A14_ENT'),2),Value(' %'), output_field=CharField())
            )
            .values(
                'Clave_de_la_entidad',
                'Nombre_de_la_entidad',
                'Población_hablante_de_lengua_indígena_de_12_a_14_años',
                'Población_de_12_a_14_años',
                'Porcentaje_hablante_de_lengua_indígena_de_12_a_14_años',
            )
        )
    elif indicador == 'Porc_hli_15A17_N': ##12
        # Consulta y renombra columnas para el indicador 'Porc_hli_3mas'
        datos = (
            Table_indicadores_Entidad.objects.annotate(
                Clave_de_la_entidad=F('CVE_ENT'),
                Nombre_de_la_entidad=F('NOM_ENT'),
                Población_hablante_de_lengua_indígena_de_15_a_17_años=F('HLI_15A17_ENT'),
                Población_de_15_a_17_años=F('POB_15A17_ENT'),
                Porcentaje_hablante_de_lengua_indígena_de_15_a_17_años=Concat(Round(F('PORC_HLI_15A17_ENT'),2),Value(' %'), output_field=CharField())
            )
            .values(
                'Clave_de_la_entidad',
                'Nombre_de_la_entidad',
                'Población_hablante_de_lengua_indígena_de_15_a_17_años',
                'Población_de_15_a_17_años',
                'Porcentaje_hablante_de_lengua_indígena_de_15_a_17_años',
            )
        )
    elif indicador == 'Porc_analfa_t_N': ##13
        # Consulta y renombra columnas para el indicador 'Porc_hli_3mas'
        datos = (
            Table_indicadores_Entidad.objects.annotate(
                Clave_de_la_entidad=F('CVE_ENT'),
                Nombre_de_la_entidad=F('NOM_ENT'),
                Porcentaje_de_analfabetismo_de_15_años_y_más=Concat(Round(F('PORC_ANALFA_T_ENT'),2),Value(' %'), output_field=CharField())
            )
            .values(
                'Clave_de_la_entidad',
                'Nombre_de_la_entidad',
                'Porcentaje_de_analfabetismo_de_15_años_y_más',
            )
        )
    elif indicador == 'Porc_analfa_h_N': ##14
        # Consulta y renombra columnas para el indicador 'Porc_hli_3mas'
        datos = (
            Table_indicadores_Entidad.objects.annotate(
                Clave_de_la_entidad=F('CVE_ENT'),
                Nombre_de_la_entidad=F('NOM_ENT'),
                Porcentaje_de_analfabetismo_15_años_y_más_por_hombre=Concat(Round(F('PORC_ANALFA_H_ENT'),2),Value(' %'), output_field=CharField())
            )
            .values(
                'Clave_de_la_entidad',
                'Nombre_de_la_entidad',
                'Porcentaje_de_analfabetismo_15_años_y_más_por_hombre',
            )
        )
    elif indicador == 'Porc_analfa_m_N': ##15
        # Consulta y renombra columnas para el indicador 'Porc_hli_3mas'
        datos = (
            Table_indicadores_Entidad.objects.annotate(
                Clave_de_la_entidad=F('CVE_ENT'),
                Nombre_de_la_entidad=F('NOM_ENT'),
                Porcentaje_de_analfabetismo_15_años_y_más_por_mujer=Concat(Round(F('PORC_ANALFA_M_ENT'),2),Value(' %'), output_field=CharField())
            )
            .values(
                'Clave_de_la_entidad',
                'Nombre_de_la_entidad',
                'Porcentaje_de_analfabetismo_15_años_y_más_por_mujer',
            )
        )
    elif indicador == 'Porc_aleb_20A24_N': ##16
        # Consulta y renombra columnas para el indicador 'Porc_hli_3mas'
        datos = (
            Table_indicadores_Entidad.objects.annotate(
                Clave_de_la_entidad=F('CVE_ENT'),
                Nombre_de_la_entidad=F('NOM_ENT'),
                Porcentaje_de_20_a_24_con_educación_básica=Concat(Round(F('PORC_ALEB_20A24_ENT'),2),Value(' %'), output_field=CharField())
            )
            .values(
                'Clave_de_la_entidad',
                'Nombre_de_la_entidad',
                'Porcentaje_de_20_a_24_con_educación_básica',
            )
        )
    elif indicador == 'Porc_alems_20A24_N': ##17
        # Consulta y renombra columnas para el indicador 'Porc_hli_3mas'
        datos = (
            Table_indicadores_Entidad.objects.annotate(
                Clave_de_la_entidad=F('CVE_ENT'),
                Nombre_de_la_entidad=F('NOM_ENT'),
                Porcentaje_de_20_a_24_con_EMS=Concat(Round(F('PORC_ALEMS_20A24_ENT'),2),Value(' %'), output_field=CharField())
            )
            .values(
                'Clave_de_la_entidad',
                'Nombre_de_la_entidad',
                'Porcentaje_de_20_a_24_con_EMS',
            )
        )
    elif indicador == 'Tasa_asis_3a5_N': ##18
        # Consulta y renombra columnas para el indicador 'Porc_hli_3mas'
        datos = (
            Table_indicadores_Entidad.objects.annotate(
                Clave_de_la_entidad=F('CVE_ENT'),
                Nombre_de_la_entidad=F('NOM_ENT'),
                Tasa_asistencia_grupo_3_a_5=Concat(Round(F('tasa_asis_3a5_ent'),2),Value(' %'), output_field=CharField())
            )
            .values(
                'Clave_de_la_entidad',
                'Nombre_de_la_entidad',
                'Tasa_asistencia_grupo_3_a_5',
            )
        )
    elif indicador == 'Tasa_asis_6a11_N': ##19
        # Consulta y renombra columnas para el indicador 'Porc_hli_3mas'
        datos = (
            Table_indicadores_Entidad.objects.annotate(
                Clave_de_la_entidad=F('CVE_ENT'),
                Nombre_de_la_entidad=F('NOM_ENT'),
                Tasa_asistencia_grupo_6_a_11=Concat(Round(F('tasa_asis_6a11_ent'),2),Value(' %'), output_field=CharField())
            )
            .values(
                'Clave_de_la_entidad',
                'Nombre_de_la_entidad',
                'Tasa_asistencia_grupo_6_a_11',
            )
        )
    elif indicador == 'Tasa_asis_12a14_N': ##20
        # Consulta y renombra columnas para el indicador 'Porc_hli_3mas'
        datos = (
            Table_indicadores_Entidad.objects.annotate(
                Clave_de_la_entidad=F('CVE_ENT'),
                Nombre_de_la_entidad=F('NOM_ENT'),
                Tasa_asistencia_grupo_12_a_14=Concat(Round(F('tasa_asis_12a14_ent'),2),Value(' %'), output_field=CharField())
            )
            .values(
                'Clave_de_la_entidad',
                'Nombre_de_la_entidad',
                'Tasa_asistencia_grupo_12_a_14',
            )
        )
    elif indicador == 'Tasa_asis_15a17_N': ##21
        # Consulta y renombra columnas para el indicador 'Porc_hli_3mas'
        datos = (
            Table_indicadores_Entidad.objects.annotate(
                Clave_de_la_entidad=F('CVE_ENT'),
                Nombre_de_la_entidad=F('NOM_ENT'),
                Tasa_asistencia_grupo_15_a_17=Concat(Round(F('tasa_asis_15a17_ent'),2),Value(' %'), output_field=CharField())
            )
            .values(
                'Clave_de_la_entidad',
                'Nombre_de_la_entidad',
                'Tasa_asistencia_grupo_15_a_17',
            )
        )
    elif indicador == 'Gpr_inegi_H_N': ##22
        # Consulta y renombra columnas para el indicador 'Porc_hli_3mas'
        datos = (
            Table_indicadores_Entidad.objects.annotate(
                Clave_de_la_entidad=F('CVE_ENT'),
                Nombre_de_la_entidad=F('NOM_ENT'),
                Grado_promedio_de_escolaridad_por_hombres_cálculo_Inegi=Concat(Round(F('GPR_INEGI_H_ENT'),2),Value(' %'), output_field=CharField())
            )
            .values(
                'Clave_de_la_entidad',
                'Nombre_de_la_entidad',
                'Grado_promedio_de_escolaridad_por_hombres_cálculo_Inegi',
            )
        )
    elif indicador == 'Gpr_inegi_M_N': ##23
        # Consulta y renombra columnas para el indicador 'Porc_hli_3mas'
        datos = (
            Table_indicadores_Entidad.objects.annotate(
                Clave_de_la_entidad=F('CVE_ENT'),
                Nombre_de_la_entidad=F('NOM_ENT'),
                Grado_promedio_de_escolaridad_por_mujeres_cálculo_Inegi=Concat(Round(F('GPR_INEGI_M_ENT'),2),Value(' %'), output_field=CharField())
            )
            .values(
                'Clave_de_la_entidad',
                'Nombre_de_la_entidad',
                'Grado_promedio_de_escolaridad_por_mujeres_cálculo_Inegi',
            )
        )
    elif indicador == 'Gpr_Inegi_T_N': ##24
        # Consulta y renombra columnas para el indicador 'Porc_hli_3mas'
        datos = (
            Table_indicadores_Entidad.objects.annotate(
                Clave_de_la_entidad=F('CVE_ENT'),
                Nombre_de_la_entidad=F('NOM_ENT'),
                Grado_promedio_de_escolaridad_cálculo_Inegi=Concat(Round(F('GPR_INEGI_T_ENT'),2),Value(' %'), output_field=CharField())
            )
            .values(
                'Clave_de_la_entidad',
                'Nombre_de_la_entidad',
                'Grado_promedio_de_escolaridad_cálculo_Inegi',
            )
        )
    else:
        # Si el indicador no coincide, retorna None
        return None

    # Renombra las claves reemplazando los guiones bajos por espacios
    datos_renombrados = [
        {clave.replace("_", " "): valor for clave, valor in fila.items()}
        for fila in datos
    ]
    return datos_renombrados

################################################################################################################
############################## Función para obtener datos por Municipios #######################################
def obtener_datos_entidad(indicador, entidad):
    if indicador == 'Porc_ind':##1
        # Realiza la consulta filtrando por el nombre de la entidad y renombrando las columnas utilizando 'annotate
        datos = (
            Table_indicadores.objects.filter(NOM_ENT=entidad).annotate(
                    Clave_de_la_entidad=F('CVE_ENT'),
                    Nombre_de_la_entidad=F('NOM_ENT'),
                    Clave_del_municipio=F('CVE_MUN'),
                    Nombre_del_municipio=F('NOM_MUN'),
                    Población_indígena=F('INDIGENA'),
                    Población_total=F('POB_TOTAL'),
                    Porcentaje_de_población_indígena=Concat(Round(F('PORC_IND'),2), Value(' %'), output_field=CharField())
            ) # Renombra las columnas utilizando la función F
            .values('Clave_de_la_entidad',
                    'Nombre_de_la_entidad',
                    'Clave_del_municipio',
                    'Nombre_del_municipio',
                    'Población_indígena',
                    'Población_total',
                    'Porcentaje_de_población_indígena',
            ) # Selecciona las columnas con los nuevos nombres
        )    
    elif indicador == 'Porc_no_ind':##2
        # Realiza la consulta filtrando por el nombre de la entidad y renombrando las columnas utilizando 'annotate
        datos = (
            Table_indicadores.objects.filter(NOM_ENT=entidad).annotate(
                    Clave_de_la_entidad=F('CVE_ENT'),
                    Nombre_de_la_entidad=F('NOM_ENT'),
                    Clave_del_municipio=F('CVE_MUN'),
                    Nombre_del_municipio=F('NOM_MUN'),
                    Población_no_indígena=F('NO_IND'),
                    Población_total=F('POB_TOTAL'),
                    Porcentaje_de_población_no_indígena=Concat(Round(F('PORC_NO_IND'),2), Value(' %'), output_field=CharField())
                )# Renombra las columnas utilizando la función F
            .values('Clave_de_la_entidad','Nombre_de_la_entidad',
                    'Clave_del_municipio',
                    'Nombre_del_municipio',
                    'Población_no_indígena',
                    'Población_total',
                    'Porcentaje_de_población_no_indígena',
            ) # Selecciona las columnas con los nuevos nombres
        )
    elif indicador == 'Porc_hli_3mas':##3
        # Realiza la consulta filtrando por el nombre de la entidad y renombrando las columnas utilizando 'annotate
        datos = (
            Table_indicadores.objects.filter(NOM_ENT=entidad).annotate(
                    Clave_de_la_entidad=F('CVE_ENT'),
                    Nombre_de_la_entidad=F('NOM_ENT'),
                    Clave_del_municipio=F('CVE_MUN'),
                    Nombre_del_municipio=F('NOM_MUN'),
                    Hablantes_de_lengua_indígena_de_3_años_y_más=F('HLI_3YMAS'),
                    Población_de_3_y_más_años=F('POB3YMAS'),
                    Porcentaje_de_hablantes_de_lengua_indígena_de_3_años_y_más=Concat(Round(F('PORC_HLI_3mas'),2), Value(' %'), output_field=CharField())
                )# Renombra las columnas utilizando la función F
            .values('Clave_de_la_entidad',
                    'Nombre_de_la_entidad',
                    'Clave_del_municipio',
                    'Nombre_del_municipio',
                    'Hablantes_de_lengua_indígena_de_3_años_y_más',
                    'Población_de_3_y_más_años',
                    'Porcentaje_de_hablantes_de_lengua_indígena_de_3_años_y_más',)# Selecciona las columnas con los nuevos nombres
        )
        # Renombramos las claves de los datos obtenidos
    elif indicador == 'Porc_no_hli':##4
        # Realiza la consulta filtrando por el nombre de la entidad y renombrando las columnas utilizando 'annotate
        datos = (
            Table_indicadores.objects.filter(NOM_ENT=entidad).annotate(
                    Clave_de_la_entidad=F('CVE_ENT'),
                    Nombre_de_la_entidad=F('NOM_ENT'),
                    Clave_del_municipio=F('CVE_MUN'),
                    Nombre_del_municipio=F('NOM_MUN'),
                    No_hablantes_de_lengua_indígena_de_3_años_y_más=F('NO_HLI'),
                    Población_de_3_y_más_años=F('POB3YMAS'),
                    Porcentaje_de_no_hablantes_de_lengua_indígena_de_3_años_y_más=Concat(Round(F('PORC_NO_HLI'),2), Value(' %'), output_field=CharField())
                )# Renombra las columnas utilizando la función F
            .values('Clave_de_la_entidad',
                    'Nombre_de_la_entidad',
                    'Clave_del_municipio',
                    'Nombre_del_municipio',
                    'No_hablantes_de_lengua_indígena_de_3_años_y_más',
                    'Población_de_3_y_más_años',
                    'Porcentaje_de_no_hablantes_de_lengua_indígena_de_3_años_y_más',)# Selecciona las columnas con los nuevos nombres
        )
    elif indicador == 'Porc_ne_hli':##5
        # Realiza la consulta filtrando por el nombre de la entidad y renombrando las columnas utilizando 'annotate
        datos = (
            Table_indicadores.objects.filter(NOM_ENT=entidad).annotate(
                    Clave_de_la_entidad=F('CVE_ENT'),
                    Nombre_de_la_entidad=F('NOM_ENT'),
                    Clave_del_municipio=F('CVE_MUN'),
                    Nombre_del_municipio=F('NOM_MUN'),
                    Condición_hablante_de_lengua_indígena_no_especificada_de_3_años_y_más=F('NE_HLI'),
                    Población_de_3_y_más_años=F('POB3YMAS'),
                    Porcentaje_de_condición_hablante_de_lengua_indígena_de_3_años_y_más_no_especificada=Concat(Round(F('PORC_NE_HLI'),2), Value(' %'), output_field=CharField())
                )# Renombra las columnas utilizando la función F
            .values('Clave_de_la_entidad',
                    'Nombre_de_la_entidad',
                    'Clave_del_municipio',
                    'Nombre_del_municipio',
                    'Condición_hablante_de_lengua_indígena_no_especificada_de_3_años_y_más',
                    'Población_de_3_y_más_años',
                    'Porcentaje_de_condición_hablante_de_lengua_indígena_de_3_años_y_más_no_especificada',)# Selecciona las columnas con los nuevos nombres
        )
    elif indicador == 'Porc_hli_3mas_espa':##6
        # Realiza la consulta filtrando por el nombre de la entidad y renombrando las columnas utilizando 'annotate
        datos = (
            Table_indicadores.objects.filter(NOM_ENT=entidad).annotate(
                    Clave_de_la_entidad=F('CVE_ENT'),
                    Nombre_de_la_entidad=F('NOM_ENT'),
                    Clave_del_municipio=F('CVE_MUN'),
                    Nombre_del_municipio=F('NOM_MUN'),
                    Hablantes_de_lengua_indígena_y_de_español_de_3_años_y_más=F('HLI_3mas_espa'),
                    Hablantes_de_lengua_indígena_de_3_años_y_más=F('HLI_3YMAS'),
                    Porcentaje_de_hablantes_de_lengua_indígena_y_de_español_de_3_años_y_más=Concat(Round(F('PORC_HLI_3mas_espa'),2), Value(' %'), output_field=CharField())
                )# Renombra las columnas utilizando la función F
            .values('Clave_de_la_entidad',
                    'Nombre_de_la_entidad',
                    'Clave_del_municipio',
                    'Nombre_del_municipio',
                    'Hablantes_de_lengua_indígena_y_de_español_de_3_años_y_más',
                    'Hablantes_de_lengua_indígena_de_3_años_y_más',
                    'Porcentaje_de_hablantes_de_lengua_indígena_y_de_español_de_3_años_y_más',)# Selecciona las columnas con los nuevos nombres
        )
    elif indicador == 'Porc_hli_3mas_Noespa':##7
        # Realiza la consulta filtrando por el nombre de la entidad y renombrando las columnas utilizando 'annotate'
        datos = (
            Table_indicadores.objects.filter(NOM_ENT=entidad).annotate(
                    Clave_de_la_entidad=F('CVE_ENT'),
                    Nombre_de_la_entidad=F('NOM_ENT'),
                    Clave_del_municipio=F('CVE_MUN'),
                    Nombre_del_municipio=F('NOM_MUN'),
                    Hablantes_de_lengua_indígena_monolingües=F('HLI_3mas_Noespa'),
                    Hablantes_de_lengua_indígena_de_3_años_y_más=F('HLI_3YMAS'),
                    Porcentaje_de_hablantes_de_lengua_indígena_monolingües=Concat(Round(F('PORC_HLI_3mas_Noespa'),2), Value(' %'), output_field=CharField())
                )# Renombra las columnas utilizando la función F
            .values('Clave_de_la_entidad',
                    'Nombre_de_la_entidad',
                    'Clave_del_municipio',
                    'Nombre_del_municipio',
                    'Hablantes_de_lengua_indígena_monolingües',
                    'Hablantes_de_lengua_indígena_de_3_años_y_más',
                    'Porcentaje_de_hablantes_de_lengua_indígena_monolingües',)# Selecciona las columnas con los nuevos nombres
        )
    elif indicador == 'PorcC_hli_3mas_NE':##8
        # Realiza la consulta filtrando por el nombre de la entidad y renombrando las columnas utilizando 'annotate
        datos = (
            Table_indicadores.objects.filter(NOM_ENT=entidad).annotate(
                    Clave_de_la_entidad=F('CVE_ENT'),
                    Nombre_de_la_entidad=F('NOM_ENT'),
                    Clave_del_municipio=F('CVE_MUN'),
                    Nombre_del_municipio=F('NOM_MUN'),
                    Condición_hablante_de_español_no_especificada_de_3_años_y_más=F('HLI_3mas_NE'),
                    Hablantes_de_lengua_indígena_de_3_años_y_más=F('HLI_3YMAS'),
                    Porcentaje_de_condición_hablante_de_español_de_3_años_y_más_no_especificada=Concat(Round(F('PORC_HLI_3mas_NE'),2), Value(' %'), output_field=CharField())
                )# Renombra las columnas utilizando la función F
            .values('Clave_de_la_entidad',
                    'Nombre_de_la_entidad',
                    'Clave_del_municipio',
                    'Nombre_del_municipio',
                    'Condición_hablante_de_español_no_especificada_de_3_años_y_más',
                    'Hablantes_de_lengua_indígena_de_3_años_y_más',
                    'Porcentaje_de_condición_hablante_de_español_de_3_años_y_más_no_especificada',)# Selecciona las columnas con los nuevos nombres
        )
    elif indicador == 'Porc_hli_3A5':##9
        # Realiza la consulta filtrando por el nombre de la entidad y renombrando las columnas utilizando 'annotate
        datos = (
            Table_indicadores.objects.filter(NOM_ENT=entidad).annotate(
                    Clave_de_la_entidad=F('CVE_ENT'),
                    Nombre_de_la_entidad=F('NOM_ENT'),
                    Clave_del_municipio=F('CVE_MUN'),
                    Nombre_del_municipio=F('NOM_MUN'),
                    Población_hablante_de_lengua_indígena_de_3_a_5_años=F('HLI_3A5'),
                    Población_de_3_a_5_años=F('POB_3A5'),
                    Porcentaje_hablante_de_lengua_indígena_de_3_a_5_años=Concat(Round(F('PORC_HLI_3A5'),2), Value(' %'), output_field=CharField())
                )# Renombra las columnas utilizando la función F
            .values('Clave_de_la_entidad',
                    'Nombre_de_la_entidad',
                    'Clave_del_municipio',
                    'Nombre_del_municipio',
                    'Población_hablante_de_lengua_indígena_de_3_a_5_años',
                    'Población_de_3_a_5_años',
                    'Porcentaje_hablante_de_lengua_indígena_de_3_a_5_años',)# Selecciona las columnas con los nuevos nombres
        )
    elif indicador == 'Porc_hli_6A11':##10
        # Realiza la consulta filtrando por el nombre de la entidad y renombrando las columnas utilizando 'annotate
        datos = (
            Table_indicadores.objects.filter(NOM_ENT=entidad).annotate(
                    Clave_de_la_entidad=F('CVE_ENT'),
                    Nombre_de_la_entidad=F('NOM_ENT'),
                    Clave_del_municipio=F('CVE_MUN'),
                    Nombre_del_municipio=F('NOM_MUN'),
                    Población_hablante_de_lengua_indígena_de_6_a_11_años=F('HLI_6A11'),
                    Población_de_6_a_11_años=F('POB_6A11'),
                    Porcentaje_hablante_de_lengua_indígena_de_6_a_11_años=Concat(Round(F('PORC_HLI_6A11'),2), Value(' %'), output_field=CharField())
                )# Renombra las columnas utilizando la función F
            .values('Clave_de_la_entidad',
                    'Nombre_de_la_entidad',
                    'Clave_del_municipio',
                    'Nombre_del_municipio',
                    'Población_hablante_de_lengua_indígena_de_6_a_11_años',
                    'Población_de_6_a_11_años',
                    'Porcentaje_hablante_de_lengua_indígena_de_6_a_11_años',)# Selecciona las columnas con los nuevos nombres
        )
    elif indicador == 'Porc_hli_12A14':##11
        # Realiza la consulta filtrando por el nombre de la entidad y renombrando las columnas utilizando 'annotate
        datos = (
            Table_indicadores.objects.filter(NOM_ENT=entidad).annotate(
                    Clave_de_la_entidad=F('CVE_ENT'),
                    Nombre_de_la_entidad=F('NOM_ENT'),
                    Clave_del_municipio=F('CVE_MUN'),
                    Nombre_del_municipio=F('NOM_MUN'),
                    Población_hablante_de_lengua_indígena_de_12_a_14_años=F('HLI_12A14'),
                    Población_de_12_a_14_años=F('POB_12A14'),
                    Porcentaje_hablante_de_lengua_indígena_de_12_a_14_años=Concat(Round(F('PORC_HLI_12A14'),2), Value(' %'), output_field=CharField())
                )# Renombra las columnas utilizando la función F
            .values('Clave_de_la_entidad',
                    'Nombre_de_la_entidad',
                    'Clave_del_municipio',
                    'Nombre_del_municipio',
                    'Población_hablante_de_lengua_indígena_de_12_a_14_años',
                    'Población_de_12_a_14_años',
                    'Porcentaje_hablante_de_lengua_indígena_de_12_a_14_años',)# Selecciona las columnas con los nuevos nombres
        )
    elif indicador == 'Porc_hli_15A17':##12
        # Realiza la consulta filtrando por el nombre de la entidad y renombrando las columnas utilizando 'annotate
        datos = (
            Table_indicadores.objects.filter(NOM_ENT=entidad).annotate(
                    Clave_de_la_entidad=F('CVE_ENT'),
                    Nombre_de_la_entidad=F('NOM_ENT'),
                    Clave_del_municipio=F('CVE_MUN'),
                    Nombre_del_municipio=F('NOM_MUN'),
                    Población_hablante_de_lengua_indígena_de_15_a_17_años=F('HLI_15A17'),
                    Población_de_15_a_17_años=F('POB_15A17'),
                    Porcentaje_hablante_de_lengua_indígena_de_15_a_17_años=Concat(Round(F('PORC_HLI_15A17'),2), Value(' %'), output_field=CharField())
                )# Renombra las columnas utilizando la función F
            .values('Clave_de_la_entidad',
                    'Nombre_de_la_entidad',
                    'Clave_del_municipio',
                    'Nombre_del_municipio',
                    'Población_hablante_de_lengua_indígena_de_15_a_17_años',
                    'Población_de_15_a_17_años',
                    'Porcentaje_hablante_de_lengua_indígena_de_15_a_17_años',)# Selecciona las columnas con los nuevos nombres
        )
    elif indicador == 'Porc_analfa_t':##13
        # Realiza la consulta filtrando por el nombre de la entidad y renombrando las columnas utilizando 'annotate
        datos = (
            Table_indicadores.objects.filter(NOM_ENT=entidad).annotate(
                    Clave_de_la_entidad=F('CVE_ENT'),
                    Nombre_de_la_entidad=F('NOM_ENT'),
                    Clave_del_municipio=F('CVE_MUN'),
                    Nombre_del_municipio=F('NOM_MUN'),
                    Porcentaje_de_analfabetismo_de_15_años_y_más=Concat(Round(F('PORC_ANALFA_T'),2), Value(' %'), output_field=CharField())
                )# Renombra las columnas utilizando la función F
            .values('Clave_de_la_entidad',
                    'Nombre_de_la_entidad',
                    'Clave_del_municipio',
                    'Nombre_del_municipio',
                    'Porcentaje_de_analfabetismo_de_15_años_y_más',)# Selecciona las columnas con los nuevos nombres
        )
    elif indicador == 'Porc_analfa_h':##14
        # Realiza la consulta filtrando por el nombre de la entidad y renombrando las columnas utilizando 'annotate
        datos = (
            Table_indicadores.objects.filter(NOM_ENT=entidad).annotate(
                    Clave_de_la_entidad=F('CVE_ENT'),
                    Nombre_de_la_entidad=F('NOM_ENT'),
                    Clave_del_municipio=F('CVE_MUN'),
                    Nombre_del_municipio=F('NOM_MUN'),
                    Porcentaje_de_analfabetismo_15_años_y_más_por_hombre=Concat(Round(F('PORC_ANALFA_H'),2), Value(' %'), output_field=CharField())
                )# Renombra las columnas utilizando la función F
            .values('Clave_de_la_entidad',
                    'Nombre_de_la_entidad',
                    'Clave_del_municipio',
                    'Nombre_del_municipio',
                    'Porcentaje_de_analfabetismo_15_años_y_más_por_hombre',)# Selecciona las columnas con los nuevos nombres
        )
    elif indicador == 'Porc_analfa_m':##15
        # Realiza la consulta filtrando por el nombre de la entidad y renombrando las columnas utilizando 'annotate
        datos = (
            Table_indicadores.objects.filter(NOM_ENT=entidad).annotate(
                    Clave_de_la_entidad=F('CVE_ENT'),
                    Nombre_de_la_entidad=F('NOM_ENT'),
                    Clave_del_municipio=F('CVE_MUN'),
                    Nombre_del_municipio=F('NOM_MUN'),
                    Porcentaje_de_analfabetismo_15_años_y_más_por_mujer=Concat(Round(F('PORC_ANALFA_M'),2), Value(' %'), output_field=CharField())
                )# Renombra las columnas utilizando la función F
            .values('Clave_de_la_entidad',
                    'Nombre_de_la_entidad',
                    'Clave_del_municipio',
                    'Nombre_del_municipio',
                    'Porcentaje_de_analfabetismo_15_años_y_más_por_mujer',)# Selecciona las columnas con los nuevos nombres
        )
    elif indicador == 'Porc_aleb_20A24':##16
        # Realiza la consulta filtrando por el nombre de la entidad y renombrando las columnas utilizando 'annotate
        datos = (
            Table_indicadores.objects.filter(NOM_ENT=entidad).annotate(
                    Clave_de_la_entidad=F('CVE_ENT'),
                    Nombre_de_la_entidad=F('NOM_ENT'),
                    Clave_del_municipio=F('CVE_MUN'),
                    Nombre_del_municipio=F('NOM_MUN'),
                    Porcentaje_de_20_a_24_con_educación_básica=Concat(Round(F('PORC_ALEB_20A24'),2), Value(' %'), output_field=CharField())
                )# Renombra las columnas utilizando la función F
            .values('Clave_de_la_entidad',
                    'Nombre_de_la_entidad',
                    'Clave_del_municipio',
                    'Nombre_del_municipio',
                    'Porcentaje_de_20_a_24_con_educación_básica',)# Selecciona las columnas con los nuevos nombres
        )
    elif indicador == 'Porc_alems_20A24':##17
        # Realiza la consulta filtrando por el nombre de la entidad y renombrando las columnas utilizando 'annotate
        datos = (
            Table_indicadores.objects.filter(NOM_ENT=entidad).annotate(
                    Clave_de_la_entidad=F('CVE_ENT'),
                    Nombre_de_la_entidad=F('NOM_ENT'),
                    Clave_del_municipio=F('CVE_MUN'),
                    Nombre_del_municipio=F('NOM_MUN'),
                    Porcentaje_de_20_a_24_con_EMS=Concat(Round(F('PORC_ALEMS_20A24'),2), Value(' %'), output_field=CharField())
                )# Renombra las columnas utilizando la función F
            .values('Clave_de_la_entidad',
                    'Nombre_de_la_entidad',
                    'Clave_del_municipio',
                    'Nombre_del_municipio',
                    'Porcentaje_de_20_a_24_con_EMS',)# Selecciona las columnas con los nuevos nombres
        )
    elif indicador == 'Tasa_asis_3a5':##18
        # Realiza la consulta filtrando por el nombre de la entidad y renombrando las columnas utilizando 'annotate
        datos = (
            Table_indicadores.objects.filter(NOM_ENT=entidad).annotate(
                    Clave_de_la_entidad=F('CVE_ENT'),
                    Nombre_de_la_entidad=F('NOM_ENT'),
                    Clave_del_municipio=F('CVE_MUN'),
                    Nombre_del_municipio=F('NOM_MUN'),
                    Tasa_asistencia_grupo_3_a_5=Concat(Round(F('tasa_asis_3a5'),2), Value(' %'), output_field=CharField())
                )# Renombra las columnas utilizando la función F
            .values('Clave_de_la_entidad',
                    'Nombre_de_la_entidad',
                    'Clave_del_municipio',
                    'Nombre_del_municipio',
                    'Tasa_asistencia_grupo_3_a_5',)# Selecciona las columnas con los nuevos nombres
        )
    elif indicador == 'Tasa_asis_6a11':##19
        # Realiza la consulta filtrando por el nombre de la entidad y renombrando las columnas utilizando 'annotate
        datos = (
            Table_indicadores.objects.filter(NOM_ENT=entidad).annotate(
                    Clave_de_la_entidad=F('CVE_ENT'),
                    Nombre_de_la_entidad=F('NOM_ENT'),
                    Clave_del_municipio=F('CVE_MUN'),
                    Nombre_del_municipio=F('NOM_MUN'),
                    Tasa_asistencia_grupo_6_a_11=Concat(Round(F('tasa_asis_6a11'),2), Value(' %'), output_field=CharField())
                )# Renombra las columnas utilizando la función F
            .values('Clave_de_la_entidad',
                    'Nombre_de_la_entidad',
                    'Clave_del_municipio',
                    'Nombre_del_municipio',
                    'Tasa_asistencia_grupo_6_a_11',)# Selecciona las columnas con los nuevos nombres
        )
    elif indicador == 'Tasa_asis_12a14':##20
        # Realiza la consulta filtrando por el nombre de la entidad y renombrando las columnas utilizando 'annotate
        datos = (
            Table_indicadores.objects.filter(NOM_ENT=entidad).annotate(
                    Clave_de_la_entidad=F('CVE_ENT'),
                    Nombre_de_la_entidad=F('NOM_ENT'),
                    Clave_del_municipio=F('CVE_MUN'),
                    Nombre_del_municipio=F('NOM_MUN'),
                    Tasa_asistencia_grupo_12_a_14=Concat(Round(F('tasa_asis_12a14'),2), Value(' %'), output_field=CharField())
                )# Renombra las columnas utilizando la función F
            .values('Clave_de_la_entidad',
                    'Nombre_de_la_entidad',
                    'Clave_del_municipio',
                    'Nombre_del_municipio',
                    'Tasa_asistencia_grupo_12_a_14',)# Selecciona las columnas con los nuevos nombres
        )
    elif indicador == 'Tasa_asis_15a17':##21
        # Realiza la consulta filtrando por el nombre de la entidad y renombrando las columnas utilizando 'annotate
        datos = (
            Table_indicadores.objects.filter(NOM_ENT=entidad).annotate(
                    Clave_de_la_entidad=F('CVE_ENT'),
                    Nombre_de_la_entidad=F('NOM_ENT'),
                    Clave_del_municipio=F('CVE_MUN'),
                    Nombre_del_municipio=F('NOM_MUN'),
                    Tasa_asistencia_grupo_15_a_17=Concat(Round(F('tasa_asis_15a17'),2), Value(' %'), output_field=CharField())
                )# Renombra las columnas utilizando la función F
            .values('Clave_de_la_entidad',
                    'Nombre_de_la_entidad',
                    'Clave_del_municipio',
                    'Nombre_del_municipio',
                    'Tasa_asistencia_grupo_15_a_17',)# Selecciona las columnas con los nuevos nombres
        )
    elif indicador == 'Gpr_inegi_H':##22
        # Realiza la consulta filtrando por el nombre de la entidad y renombrando las columnas utilizando 'annotate
        datos = (
            Table_indicadores.objects.filter(NOM_ENT=entidad).annotate(
                    Clave_de_la_entidad=F('CVE_ENT'),
                    Nombre_de_la_entidad=F('NOM_ENT'),
                    Clave_del_municipio=F('CVE_MUN'),
                    Nombre_del_municipio=F('NOM_MUN'),
                    Grado_promedio_de_escolaridad_por_hombres_cálculo_Inegi=Concat(Round(F('GPR_Inegi_H'),2), Value(' %'), output_field=CharField())
                )# Renombra las columnas utilizando la función F
            .values('Clave_de_la_entidad',
                    'Nombre_de_la_entidad',
                    'Clave_del_municipio',
                    'Nombre_del_municipio',
                    'Grado_promedio_de_escolaridad_por_hombres_cálculo_Inegi',)# Selecciona las columnas con los nuevos nombres
        )
    elif indicador == 'Gpr_inegi_M':##23
        # Realiza la consulta filtrando por el nombre de la entidad y renombrando las columnas utilizando 'annotate
        datos = (
            Table_indicadores.objects.filter(NOM_ENT=entidad).annotate(
                    Clave_de_la_entidad=F('CVE_ENT'),
                    Nombre_de_la_entidad=F('NOM_ENT'),
                    Clave_del_municipio=F('CVE_MUN'),
                    Nombre_del_municipio=F('NOM_MUN'),
                    Grado_promedio_de_escolaridad_por_mujeres_cálculo_Inegi=Concat(Round(F('GPR_Inegi_M'),2), Value(' %'), output_field=CharField())
                )# Renombra las columnas utilizando la función F
            .values('Clave_de_la_entidad',
                    'Nombre_de_la_entidad',
                    'Clave_del_municipio',
                    'Nombre_del_municipio',
                    'Grado_promedio_de_escolaridad_por_mujeres_cálculo_Inegi',)# Selecciona las columnas con los nuevos nombres
        )
    elif indicador == 'Gpr_Inegi_T':##24
        # Realiza la consulta filtrando por el nombre de la entidad y renombrando las columnas utilizando 'annotate
        datos = (
            Table_indicadores.objects.filter(NOM_ENT=entidad).annotate(
                    Clave_de_la_entidad=F('CVE_ENT'),
                    Nombre_de_la_entidad=F('NOM_ENT'),
                    Clave_del_municipio=F('CVE_MUN'),
                    Nombre_del_municipio=F('NOM_MUN'),
                    Grado_promedio_de_escolaridad_cálculo_Inegi=Concat(Round(F('GPR_Inegi_T'),2), Value(' %'), output_field=CharField())
                )# Renombra las columnas utilizando la función F
            .values('Clave_de_la_entidad',
                    'Nombre_de_la_entidad',
                    'Clave_del_municipio',
                    'Nombre_del_municipio',
                    'Grado_promedio_de_escolaridad_cálculo_Inegi',)# Selecciona las columnas con los nuevos nombres
        )
    else:
        # Si el indicador no coincide, retorna None
        return None
    # Renombra las claves reemplazando los guiones bajos por espacios
    datos_renombrados = [
        {clave.replace("_", " "): valor for clave, valor in fila.items()}
        for fila in datos
    ]
    return datos_renombrados



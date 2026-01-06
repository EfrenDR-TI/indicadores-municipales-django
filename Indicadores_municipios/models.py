from django.db import models

# Create your models here.

class Table_indicadores_Entidad(models.Model):

    """
    Indicadores agregados a nivel entidad federativa.

    Contiene variables demográficas, educativas y de población indígena
    utilizadas para análisis comparativo entre entidades.
    
    Fuente principal: 
        - MEJOREDU  
          
    Cálculos con base en:
        - Metodología del INPI y cifras censales 2020.
        - Índice de Marginación por Municipio 2020 (CONAPO, 2022).
        - Censo de Población y Vivienda 2020 (INEGI, 2021); Indicadores Socioeconómicos de los pueblos Indígenas y afromexicano 2020(INPI, 2022).
        - Estadísticas Continuas del Formato 911 (fin del ciclo escolar 2019-2020 e inicio del ciclo escolar 2020-2021)(SEP-DGPPYEE, 2021).
    """
    COD_ENT = models.CharField(max_length=10)
    CVE_ENT = models.CharField(max_length=2)
    NOM_ENT = models.CharField(max_length=100)
    Abreviado_Entidad = models.CharField(max_length=2)
    Pob_Ind = models.FloatField()
    GPR_INEGI_T_ENT = models.FloatField()
    GPR_INEGI_H_ENT = models.FloatField()
    GPR_INEGI_M_ENT = models.FloatField()
    PORC_ANALFA_T_ENT = models.FloatField()  
    PORC_ANALFA_H_ENT = models.FloatField()  
    PORC_ANALFA_M_ENT = models.FloatField()  
    PORC_ALEB_20A24_ENT = models.FloatField()
    PORC_ALEMS_20A24_ENT = models.FloatField()   
    tasa_asis_3a5_ent = models.FloatField()  
    tasa_asis_6a11_ent = models.FloatField() 
    tasa_asis_12a14_ent = models.FloatField()
    tasa_asis_15a17_ent = models.FloatField()
    INDIGENA_ENT = models.IntegerField()   
    NO_IND_ENT = models.IntegerField() 
    POB_TOTAL_ENT = models.IntegerField()  
    PORC_IND_ENT = models.FloatField()   
    PORC_NO_IND_ENT = models.FloatField()
    HLI_3YMAS_ENT = models.IntegerField()  
    NO_HLI_ENT = models.IntegerField() 
    NE_HLI_ENT = models.IntegerField() 
    POB3YMAS_ENT = models.IntegerField()   
    porc_hli_3mas_ENT = models.FloatField()  
    porc_no_hli_ENT = models.FloatField()
    porc_ne_hli_ENT = models.FloatField()
    HLI_3mas_espa_ENT = models.IntegerField()  
    HLI_3mas_Noespa_ENT = models.IntegerField()
    HLI_3mas_NE_ENT = models.IntegerField()
    porc_hli_3mas_espa_ENT = models.FloatField() 
    porc_hii_3mas_Noespa_ENT = models.FloatField()   
    Porc_hli_3mas_NE_ENT = models.FloatField()   
    HLI_3A5_ENT = models.IntegerField()
    POB_3A5_ENT = models.IntegerField()
    PORC_HLI_3A5_ENT = models.FloatField()   
    HLI_6A11_ENT = models.IntegerField()   
    POB_6A11_ENT = models.IntegerField()   
    PORC_HLI_6A11_ENT = models.FloatField()  
    HLI_12A14_ENT = models.IntegerField()  
    POB_12A14_ENT = models.IntegerField()  
    PORC_HLI_12A14_ENT = models.FloatField()
    HLI_15A17_ENT = models.IntegerField()  
    POB_15A17_ENT = models.IntegerField()  
    PORC_HLI_15A17_ENT = models.FloatField() 



class Table_indicadores(models.Model):

    """
    Indicadores agregados a nivel municipal.

    Cada registro representa información sociodemográfica
    y educativa de un municipio para análisis territorial.
    
    Fuente principal: 
        - MEJOREDU    

    Cálculos con base en:
        - Metodología del INPI y cifras censales 2020.
        - Índice de Marginación por Municipio 2020 (CONAPO, 2022).
        - Censo de Población y Vivienda 2020 (INEGI, 2021); Indicadores Socioeconómicos de los pueblos Indígenas y afromexicano 2020(INPI, 2022).
        - Estadísticas Continuas del Formato 911 (fin del ciclo escolar 2019-2020 e inicio del ciclo escolar 2020-2021)(SEP-DGPPYEE, 2021).
    """
    CLAVE = models.CharField(max_length=5)
    NOM_ENT = models.CharField(max_length=100)
    CVE_ENT = models.CharField(max_length=2)
    NOM_MUN = models.CharField(max_length=100)
    CVE_MUN = models.CharField(max_length=3)
    TIPO_MUN = models.IntegerField()
    CLASIF = models.CharField(max_length=100)
    GM_2020 = models.CharField(max_length=100) 
    POB_TOTAL = models.IntegerField()
    ANALFA_15M = models.IntegerField()
    INDIGENA = models.IntegerField()
    NO_IND = models.IntegerField()
    HLI_3YMAS = models.IntegerField()
    NO_HLI = models.IntegerField()
    NE_HLI = models.IntegerField()
    POB3YMAS = models.IntegerField()
    HLI_3mas_espa = models.IntegerField()
    HLI_3mas_Noespa = models.IntegerField()
    HLI_3mas_NE = models.IntegerField()
    PORC_IND = models.FloatField()
    PORC_NO_IND = models.FloatField()
    PORC_HLI_3mas = models.FloatField()
    PORC_NO_HLI = models.FloatField()
    PORC_NE_HLI = models.FloatField()
    PORC_HLI_3mas_espa = models.FloatField()
    PORC_HLI_3mas_Noespa = models.FloatField()
    PORC_HLI_3mas_NE = models.FloatField()
    POB_0A2 = models.IntegerField()
    POB_3A5 = models.IntegerField()
    POB_6A11 = models.IntegerField()
    POB_12A14 = models.IntegerField()
    POB_15A17 = models.IntegerField()
    INPI_0A2 = models.IntegerField()
    INPI_3A5 = models.IntegerField()
    INPI_6A11 = models.IntegerField()
    INPI_12A14 = models.IntegerField()
    INPI_15A17 = models.IntegerField()
    HLI_3A5 = models.IntegerField()   
    HLI_6A11 = models.IntegerField()
    HLI_12A14 = models.IntegerField()
    HLI_15A17 = models.IntegerField()
    PORC_HLI_3A5 = models.FloatField()
    PORC_HLI_6A11 = models.FloatField()
    PORC_HLI_12A14 = models.FloatField()
    PORC_HLI_15A17 = models.FloatField()
    GPR_Inegi_T = models.FloatField()
    GPR_Inegi_H = models.FloatField()
    GPR_Inegi_M = models.FloatField()
    GPR_INEGI_T_ENT = models.FloatField()
    GPR_INEGI_H_ENT = models.FloatField()
    GPR_INEGI_M_ENT = models.FloatField()
    GPR_INEGI_T_NAL = models.FloatField()
    GPR_INEGI_H_NAL = models.FloatField()
    GPR_INEGI_M_NAL = models.FloatField()
    PORC_ANALFA_T = models.FloatField()
    PORC_ANALFA_H = models.FloatField()
    PORC_ANALFA_M = models.FloatField()
    PORC_ANALFA_T_ENT = models.FloatField()
    PORC_ANALFA_H_ENT = models.FloatField()
    PORC_ANALFA_M_ENT = models.FloatField() 
    PORC_ANALFA_T_NAL = models.FloatField()
    PORC_ANALFA_H_NAL = models.FloatField()
    PORC_ANALFA_M_NAL = models.FloatField()
    PORC_ALEB_20A24 = models.FloatField()
    PORC_ALEMS_20A24 = models.FloatField()
    PORC_ALEB_20A24_ENT = models.FloatField()
    PORC_ALEMS_20A24_ENT = models.FloatField()
    PORC_ALEB_20A24_NAL = models.FloatField()
    PORC_ALEMS_20A24_NAL = models.FloatField()
    tasa_asis_3a5 = models.FloatField()
    tasa_asis_6a11 = models.FloatField()
    tasa_asis_12a14 = models.FloatField()
    tasa_asis_15a17 = models.FloatField()
    tasa_asis_3a5_ent = models.FloatField()
    tasa_asis_6a11_ent = models.FloatField()
    tasa_asis_12a14_ent = models.FloatField()
    tasa_asis_15a17_ent = models.FloatField()
    tasa_asis_3a5_nal = models.FloatField()
    tasa_asis_6a11_nal = models.FloatField()
    tasa_asis_12a14_nal = models.FloatField()
    tasa_asis_15a17_nal = models.FloatField()

    
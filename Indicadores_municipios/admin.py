from django.contrib import admin
import data_wizard

from .models import Table_indicadores, Table_indicadores_Entidad
# Register your models here.

admin.site.register(Table_indicadores)
data_wizard.register(Table_indicadores)

admin.site.register(Table_indicadores_Entidad)
data_wizard.register(Table_indicadores_Entidad)

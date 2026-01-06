# 📊 Indicadores Municipales – Django

Sistema web desarrollado en Django para la visualización de indicadores educativos y sociodemográficos a nivel nacional y municipal, integrando tablas dinámicas, mapas interactivos y gráficas, con base en información censal y metodologías oficiales.

El proyecto está orientado al análisis territorial, facilitando la consulta, comparación y exploración de indicadores por entidad federativa y municipio.

---

## 🧩 Características principales

🔍 **Filtros dinámicos por:**
- Nivel de análisis (entidad / municipio)
- Entidad federativa
- Indicador educativo o sociodemográfico

📋 **Tablas interactivas con:**
- Búsqueda
- Paginación
- Control de número de registros

🗺 **Mapas interactivos:**
- Mapa nacional por entidad federativa
- Mapas municipales por entidad
- Escalas de color dinámicas según valores del indicador

📈 **Gráficas dinámicas:**
- Visualización comparativa por entidad o municipio
- Scroll horizontal para grandes volúmenes de datos

📂 **Separación clara de capas:**
- **Backend**
  - Django
  - Modelos
  - Vistas
  - Formularios
- **Frontend**
  - HTML
  - CSS
  - JavaScript
- **Datos geográficos**
  - GeoJSON
  - JSON

---


## 🏗 Arquitectura del proyecto

```text
Proyecto_Django/
│
├── Fichas_Municipal/              # Configuración principal del proyecto Django
├── Indicadores_municipios/        # App principal de indicadores
│   ├── models.py                  # Modelos de datos
│   ├── views.py                   # Lógica de visualización
│   ├── forms.py                   # Formularios dinámicos
│   ├── urls.py                    # Rutas de la aplicación
│   ├── templates/                 # Plantillas HTML
│   └── static/                    # Archivos estáticos (CSS, JS, imágenes)
│
├── static/
│   └── data/                      # Mapas GeoJSON / JSON por entidad
│
├── datawizard/                    # Archivos de carga de datos (Excel)
├── manage.py
└── README.md
```
## 🗂 Fuentes de información

Los indicadores presentados se construyen con base en:
- Censo de Población y Vivienda 2020 (INEGI)
- Metodología del INPI
- Índice de Marginación por Municipio 2020 (CONAPO, 2022)
- Formato 911 – Estadísticas educativas (SEP)

## 🛠 Tecnologías utilizadas

Backend
- Python
- Django

Frontend
- HTML5
- CSS3
- JavaScript

Visualización
- Highcharts
- Highmaps

Datos geoespaciales
- GeoJSON
- JSON

Base de datos
- SQLite (entorno de desarrollo)

Carga de datos
- Django Data Wizard


## 🚀 Instalación y ejecución local


### Clonar el repositorio
```bash
git clone https://github.com/EfrenDR-TI/indicadores-municipales-django.git
``` 
### Entrar al proyecto
```bash
cd indicadores-municipales-django
```
### Crear y activar entorno virtual (opcional)

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

Instalar dependencias
```bash
pip install -r requirements.txt
```
Ejecutar el servidor
```bash
python manage.py runserver
```
Acceder en el navegador a:
```bash
http://127.0.0.1:8000/
```

## 📸 Capturas de pantalla

- Mapa nacional por entidad
- Mapa municipal por entidad seleccionada
- Gráfica comparativa de indicadores
- Tabla con filtros aplicados


## 📄 Documentación adicional

El análisis detallado del proyecto, estructura de datos y decisiones de diseño se encuentra documentado en un archivo PDF independiente:

📄 **Documento:**  
docs/Analisis_Proyecto_Indicadores_Municipales.pdf

## 👤 Autor

**Efrén Dolores**
Ingeniero en Informática
Especialista en análisis de sistemas, bases de datos y visualización de información

## 📌 Notas finales

Este proyecto forma parte de un portafolio profesional, con enfoque en:
- Análisis de requerimientos
- Tratamiento y visualización de datos
- Desarrollo de sistemas web orientados a información territorial
"""

Proyecto de análisis y visualización de indicadores municipales.
Configuración orientada a entorno de desarrollo y demostración técnica.

Autor: Efrén Dolores
"""

from pathlib import Path
import os
# --------------------------------------------------
# BASE DIRECTORY
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent


# --------------------------------------------------
# SECURITY SETTINGS (usar variables de entorno)
# --------------------------------------------------
SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "django-insecure-clave-solo-para-desarrollo"
)
DEBUG = True

ALLOWED_HOSTS = [] # Agregar dominios en producción

# --------------------------------------------------
# APPLICATION DEFINITION
# --------------------------------------------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #Apps del proyecto
    'Indicadores_municipios',

    #Librerias externas
    'data_wizard',
    'data_wizard.sources',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Fichas_Municipal.urls'

# --------------------------------------------------
# TEMPLATES
# --------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Fichas_Municipal.wsgi.application'


# --------------------------------------------------
# DATABASE
# --------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



# --------------------------------------------------
# PASSWORD VALIDATION
# --------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# --------------------------------------------------
# INTERNATIONALIZATION
# --------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# --------------------------------------------------
# STATIC FILES
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static"
    
] #se agrega para conf. archivo estático JSON

# --------------------------------------------------
# DEFAULT PRIMARY KEY
# --------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

import os
import environ
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(BASE_DIR / ".env")
env = environ.Env(DEBUG=(bool, False))

SECRET_KEY = env("SECRET_KEY")

DEBUG = env("DEBUG")

ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS = True

CSRF_TRUSTED_ORIGINS = [
    'https://*.tsi.pe',
    'http://localhost:8000',
    'http://localhost:5173',
]

BASE_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

LOCAL_APPS = [
    # "apps.user",
    "apps.person",
    "apps.medicalhistory",
]

THIRD_APPS = [
    "rest_framework",
    "rest_framework_simplejwt",
    "rest_framework.authtoken",
    "django_filters",
    "corsheaders",
    "drf_spectacular",
    'import_export',
]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "es-PE"

TIME_ZONE = "America/Lima"

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_ROOT = os.path.join (BASE_DIR / 'staticfiles')
STATICFILES_DIRS = (os.path.join (BASE_DIR / 'static'),)
STATIC_URL = '/static/'

MEDIA_ROOT = BASE_DIR / "media/"
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    "DATETIME_FORMAT": "%Y-%m-%d %H:%M:%S",
    "DATETIME_INPUT_FORMATS": ["%Y-%m-%d %H:%M:%S"],
    "DATE_FORMAT": "%Y-%m-%d",
    "DATE_INPUT_FORMATS": ["%Y-%m-%d"],
    # "DEFAULT_AUTHENTICATION_CLASSES": [
        # "rest_framework_simplejwt.authentication.JWTAuthentication",
        # "rest_framework.authentication.TokenAuthentication",
    # ],
    # "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated", ],
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_RENDERER_CLASSES": (
        # 'core.settings.secureMiddleware.HTTPSRenderer',
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
        # "drf_excel.renderers.XLSXRenderer",
    ),
}

SPECTACULAR_SETTINGS = {
    "TITLE": "DRF SALUK API",
    "DESCRIPTION": "SaluK API for managing patients and medical histories.",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    # OTHER SETTINGS
}
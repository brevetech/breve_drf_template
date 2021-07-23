from pathlib import Path

import os
import sys

import environ

from breve_drf_template.util import read_docs_md

root = environ.Path(start=__file__) - 3
env = environ.Env()
env.read_env('.env')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = root()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

#DEBUG config
DEBUG = env.bool('DEBUG', default=True)

# Application definition

INSTALLED_APPS = [
    # installed apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # drf dependency apps
    'rest_framework',
    'drf_spectacular',
    # project apps
    'breve_drf_template.apps.employee.apps.EmployeeConfig',
]

# RestAPI config
REST_FRAMEWORK = {
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 15,
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema'
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Breve Rest Template',
    'DESCRIPTION': read_docs_md('index', BASE_DIR),
    'VERSION': 'v1.0.0',
    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,
        "persistAuthorization": True,
        "displayOperationId": True,
    },
    # available SwaggerUI versions: https://github.com/swagger-api/swagger-ui/releases
    "SWAGGER_UI_DIST": "//unpkg.com/swagger-ui-dist@4.0.0-beta.0", # default
    # OTHER SETTINGS
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'breve_drf_template.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [root('templates'),],
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

WSGI_APPLICATION = 'breve_drf_template.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    root('static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'assets-root', 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'assets-root', 'media')

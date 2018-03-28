"""
Django settings for donationcoordinator project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os


class YouDidntSetYourEnvironmentVarsBro(Exception):
    def __init__(self, m):
        self.missingVar = m

    def __str__(self):
        return f"You gotta set the {self.missingVar} var!"

    def __repr__(self):
        return str(self)


REQUIRED_ENVIRONMENT_VARIABLES = [
    'SECRET_KEY',
    'OSGEO4W_ROOT',
    'GDAL_LIBRARY_PATH',
    'GEOS_LIBRARY_PATH',
    'GEOPOSITION_GOOGLE_MAPS_API_KEY',
]

for ev in REQUIRED_ENVIRONMENT_VARIABLES:
    if ev not in os.environ:
        print(YouDidntSetYourEnvironmentVarsBro(ev))

# Build paths inside the project like this: os.path.join(PROJECT_ROOT, ...)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# setup for GDAL, GEOS, etc.
OSGEO4W = os.environ['OSGEO4W_ROOT']

if not os.path.isdir(OSGEO4W):
    print("OSGEO4W aka '" + OSGEO4W + "' is not a directory.")
    print("Maybe adding '64' to it will help.")
    OSGEO4W = OSGEO4W + "64"

GDAL_LIBRARY_PATH = os.environ.get('GDAL_LIBRARY_PATH')

GEOPOSITION_GOOGLE_MAPS_API_KEY = os.environ.get('GEOPOSITION_GOOGLE_MAPS_API_KEY')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY') if 'SECRET_KEY' in os.environ else 'supersecret'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django_extensions',
    'annoying',
    'donationcoordinator',
    'donator',
    'org',
    'restaurantapp',
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

ROOT_URLCONF = 'donationcoordinator.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_ROOT, 'templates'),
        ],
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

WSGI_APPLICATION = 'donationcoordinator.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'geodjango',
        'USER': 'geodjango',
        'PASSWORD': 'geodjango',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'donator.User'

LOGIN_REDIRECT_URL = '/donator/'
LOGOUT_REDIRECT_URL = '/'

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT = ''

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join('static'),
)

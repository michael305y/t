"""
Django settings for real project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

import os


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#4&t7fst*a!8l0__szf@lus(r%-a3z_oyb*f&f!v+z7^lawrmw'

# SECURITY WARNING: don't run with debug turned on in production!
# A better way to change DEBUG option automatically depending on the environment
DEBUG = 'RENDER' not in os.environ

# to determine which hosts can access endpoints in the case of APIs
# ALLOWED_HOSTS = ['.vercel.app', '127.0.0.1']
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'elevate'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'real.urls'

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

WSGI_APPLICATION = 'real.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


# # SQLite DB
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }



# # VERCEL POSTGRES DB details
# import dj_database_url

# DATABASES = {
#     'default' : dj_database_url.parse('postgresql://postgres:fA9jbOfeCDfshcvhWpGm@containers-us-west-163.railway.app:7579/railway')
# }


# RENDER  Postgres DB details
import dj_database_url

DATABASES = {
    # 'default' : dj_database_url.parse('postgres://real_estate_so32_user:0eXEfJdLn3xMQaID7wf333QmWXYXolAA@dpg-ci64b6enqql3q386d8ng-a.oregon-postgres.render.com/real_estate_so32')
    

    'default': dj_database_url.config(
        
        default='postgres://real_estate_so32_user:0eXEfJdLn3xMQaID7wf333QmWXYXolAA@dpg-ci64b6enqql3q386d8ng-a.oregon-postgres.render.com/real_estate_so32',
        conn_max_age=600,
        conn_health_checks=True,
    )
}
                                       


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'media')
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
###############    #######################

### media files
MEDIA_URL = 'media/'
MEDIA_ROOT = 'media'      ##for local developemnts

# MEDIA_ROOT = BASE_DIR / ""



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

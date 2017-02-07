"""
Django settings for cremon project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

import socket

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm_rg6&&u(de)it7&2u2&kul$f*=$m&c443khx8$sk*m(@d4@o-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'myproject',
    'registration',
    'accounts',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'cremon.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'cremon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

if socket.gethostname() == 'vishnu':
    DEBUG = TEMPLATE_DEBUG = True
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'cremon',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',
	'OPTIONS': {
         "init_command": "SET foreign_key_checks = 0;",
    },                      # Set to empty string for default.
    }
}
elif socket.gethostname() == 'wf-103-44-220-147.webfaction.com':
    DEBUG = TEMPLATE_DEBUG = False
    ALLOWED_HOSTS = ["www.sricremon.in", "sricremon.in", "www.sricremon.com", "sricremon.com"]    
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'cremon',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'rt8055',
        'PASSWORD': 'Starthere66%',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',
	'OPTIONS': {
         "init_command": "SET foreign_key_checks = 0;",
    },                      # Set to empty string for default.
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_URL = "192.168.1.3:5000"

SITE_ID = '1'

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
ACCOUNT_ACTIVATION_DAYS = 7 
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_PATH = os.path.join(BASE_DIR,'static')

TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

STATIC_URL = '/static/' # You may find this is already defined as such.
STATICFILES_DIRS = (
    STATIC_PATH,
)

CSRF_COOKIE_DOMAIN = None

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


CSRF_COOKIE_DOMAIN = None

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.
REGISTRATION_AUTO_LOGIN = False # Automatically log the user in.
LOGIN_REDIRECT_URL = '/'

STRIPE_SECRET_KEY = "sk_test_tXCtSORPdz4nrozcoOsiCy2A"
STRIPE_PUBLISHABLE_KEY = "pk_test_giqz4Y9dhjdg6QtIUbuOBahj"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'kalamemailbox'
EMAIL_HOST_PASSWORD = 'khari123'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'contact@kalamdreamhome.com'
SERVER_EMAIL = 'contact@kalamdreamhome.com'


"""
Django settings for FoodForAll project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e3$s&q1uqps%61usf(-a^++wajh8!w(_%(zp6ea9r*=1!jl^mo'

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
    'Apidoc',
    'Common',
    'DataBase',
    'Login',
    'Mail',
    'Payment',
    'Project',
    'Upload',
    'User',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'FoodForAll.urls'

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

WSGI_APPLICATION = 'FoodForAll.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'foodforall',
        'USER': 'apex',
        'PASSWORD': 'apex08',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

IMG_DIR = os.path.join(BASE_DIR, "IMG")
DOC_DIR = os.path.join(BASE_DIR, "DOC")

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, "Static")

STATICFILES_DIRS = [
    IMG_DIR,
    DOC_DIR,
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'team08.apex@gmail.com'
EMAIL_HOST_PASSWORD = 'foodforall'

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = ["http://localhost", "http://127.0.0.1", "http://*"]
CORS_ALLOW_METHODS = [
     "DELETE",
     "GET",
     "OPTIONS",
     "PATCH",
     "POST",
     "PUT",
     "VIEW",
]
CORS_ALLOW_HEADERS = [
     "accept",
     "accept-encoding",
     "authorization",
     "content-type",
     "dnt",
     "origin",
     "user-agent",
     "x-csrftoken",
     "x-requested-with",
]

LOG_DIR = os.path.join(BASE_DIR, "LOG")

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s] - %(levelname)-8s - [%(pathname)s:%(funcName)s:%(lineno)d] - %(message)s',
        },
        'simple': {
            'format': '[%(asctime)s] - %(levelname)s - %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        #'mail_admins': {
        #    'level': 'ERROR',
        #    'class': 'django.utils.log.AdminEmailHandler',
        #},
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'standard',
            'when': 'D',
            'interval': 1,
            'backupCount': 365,
            'encoding': 'utf-8',
            'filename': os.path.join(LOG_DIR, 'server-app.log'),
        },
    },
    'loggers': {
        'standard': {
            'handlers': ['file','console'],
            'level':'INFO',
            'propagate': False,
        }
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'INFO',
        'propagate': False,
    },
}

RESOURCE_DIR = os.path.join(BASE_DIR, "Resource")

APPEND_SLASH=False
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
    'Share',
    'Upload',
    'User',
    'Statistics',
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

STATIC_ROOT = os.path.join(BASE_DIR, "STATIC")

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
CORS_ORIGIN_WHITELIST = ["http://localhost:3000", "http://127.0.0.1:3000"]
#CORS_ORIGIN_ALLOW_ALL = True
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
            'level':'DEBUG',
            'propagate': False,
        }
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'INFO',
        'propagate': False,
    },
}

VERIFY_CODE_EXPIRES = 30 * 60
VERIFY_CODE_KEY_REGIS = "regis_code"
VERIFY_CODE_KEY_RESET_PASSWORD = "reset_password_code"

MAX_FAILED_LOGIN_ATTEMPTS_ALLOWED = 10
MAX_FAILED_LOGIN_INTERVAL_ALLOWED = 5 * 60
MAX_FAILED_LOGIN_ATTEMPTS_KEY = "login_attempt"
LOGIN_FORBIDDEN_KEY = "login_forbidden"

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'default'
    },
    VERIFY_CODE_KEY_REGIS: {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': VERIFY_CODE_KEY_REGIS
    },
    VERIFY_CODE_KEY_RESET_PASSWORD: {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': VERIFY_CODE_KEY_RESET_PASSWORD
    },
    MAX_FAILED_LOGIN_ATTEMPTS_KEY: {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': MAX_FAILED_LOGIN_ATTEMPTS_KEY
    },
    LOGIN_FORBIDDEN_KEY: {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': LOGIN_FORBIDDEN_KEY
    },
}

PAYMENT_CLIENT_ID = 'AT96y4XONeD0OK88DlwW43rU3sSw9lH55Yfz3etD0RvFtTVfoUbwIpMebVjRxkmEeyFf5ycl7Xp7gU1l'
PAYMENT_CLIENT_SECRET = 'EFC8hviHQf2sFY-hl_IRkg-4mPclc5dfPxlnN6Vz70F8SHf9-hCImLfaBjqTk4m5_pXb7IujTpqo0JF-'

RESOURCE_DIR = os.path.join(BASE_DIR, "Resource")

APPEND_SLASH=False

STATUS_CODE = {"success": 0,
               "user has not logged in": 100001,
               "user update failed": 100002,
               "operation is not available to individual user": 100003,
               "user is already logged in": 100004,
               "invalid username": 100005,
               "wrong password": 100006,
               "email is already registered": 100007,
               "password setting failed": 100008,
               "email is not registered": 100009,
               "mismatch between logged in user and target user": 100010,
               "invalid user type": 100011,
               "wrong parameters for user creation": 100012,
               "user creation failed": 100013,
               "target user does not exist": 100014,
               "project creation failed": 200001,
               "project does not exist": 200002,
               "user is not the owner of the project": 200003,
               "project is not deletable": 200004,
               "project update failed": 200005,
               "project is not editable": 200006,
               "project information is incomplete": 200007,
               "project start up failed": 200008,
               "project has already started": 200009,
               "project stop failed": 200010,
               "project is not ongoing or on hold": 200011,
               "project end time is invalid": 200012,
               "project status invalid": 200013,
               "project price invalid": 200014,
               "project order invalid": 200015,
               "project is already finished": 200016,
               "project is not ongoing": 200017,
               "project suspension failed": 200018,
               "invalid currency type": 300001,
               "email delivery failed": 300002,
               "captcha verification failed": 300003,
               "invalid action": 300004,
               "write to file failed": 300005,
               "wrong region name or code": 300006,
               "invalid request parameters": 400001,
               "unable to get image file from request": 400002,
               "unable to get document file from request": 400003,
               "temporary ban due to too frequent login attempts": 400004,
               "create paypal product failed": 500001,
               "payment capture failed": 500002,
               }
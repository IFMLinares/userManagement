"""
Django settings for settings project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import settings.db as db

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')1f5gs72kk97fy@f8hfuixuf9cjyq38v6@46@ce+j#ycsdpkk+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # dashboard Django-Jet
    'jet.dashboard',
    'jet',

    # apps django // aplicaciones django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',

    # django allauth modules
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',

    # own apps // aplicaciones propias
    'apps.core'
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

ROOT_URLCONF = 'settings.urls'

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

WSGI_APPLICATION = 'settings.wsgi.application'


# Database // Base de Datos
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = db.SQLITE


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'es-ve'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# static settings
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    # Metodo de autenticación especifico de allauth, como logear por email
    'allauth.account.auth_backends.AuthenticationBackend',
)
AUTH_USER_MODEL = 'core.User'
# Django Allauth Settings
SITE_ID = 1
LOGIN_REDIRECT_URL = '/admin'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'

ACCOUNT_SIGNUP_FORM_CLASS = 'apps.core.forms.signUpForm.SignupForm'

ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 120
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_SIGNUP_REDIRECT_URL = LOGIN_REDIRECT_URL
ACCOUNT_USERNAME_MIN_LENGTH = 5
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
EMAIL_TIMEOUT = 5
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = DEFAULT_FROM_EMAIL = 'titolfalcon@gmail.com'
EMAIL_HOST_PASSWORD = '01022010ab$'
EMAIL_SUBJECT_PREFIX = 'User Management'

# crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Django-Jet settings

X_FRAME_OPTIONS = 'SAMEORIGIN'

JET_THEMES = [
    {
        'theme': 'default', # theme folder name
        'color': '#47bac1', # color of the theme's button in user menu
        'title': 'Default' # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]

JET_SIDE_MENU_COMPACT = True

JET_CHANGE_FORM_SIBLING_LINKS = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
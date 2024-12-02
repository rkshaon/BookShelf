from pathlib import Path

import os
import datetime

from BookShelf.env import DATABASES_SETTINGS
from BookShelf.env import ALLOWED_HOSTS_SETTINGS
from BookShelf.env import SECRET_KEY_SETTINGS
from BookShelf.env import CORS_ALLOWED_ORIGINS_SETTINGS
from BookShelf.env import X_FRAME_OPTIONS_SETTINGS
from BookShelf.env import ELASTICSEARCH_DSL_SETTINGS
from BookShelf.env import FRONTEND_BASE_URL_SETTINGS

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = SECRET_KEY_SETTINGS

DEBUG = True

ALLOWED_HOSTS = ALLOWED_HOSTS_SETTINGS

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
LIBRARY_APPS = [
    'rest_framework',
    'drf_yasg',
    'corsheaders',
    'django_elasticsearch_dsl',
]
PROJECT_APPS = [
    'user_api',
    'author_api',
    'publisher_api',
    'book_api',
    'activity_api',
]
INSTALLED_APPS = DJANGO_APPS + LIBRARY_APPS + PROJECT_APPS

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'BookShelf.urls'

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

WSGI_APPLICATION = 'BookShelf.wsgi.application'

DATABASES = DATABASES_SETTINGS

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PAGINATION_CLASS': 'BookShelf.utilities.pagination.Pagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': 'BookShelf.utilities.filters.SearchFilter',
}

SIMPLE_JWT = {
    # Token lifetime, adjust as needed
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=7),
    # Set to True if you want new refresh tokens
    # every time the old ones are used
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,  # Use with token blacklisting
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

ELASTICSEARCH_DSL = ELASTICSEARCH_DSL_SETTINGS

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',           # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',          # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',         # noqa
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CORS_ALLOWED_ORIGINS = CORS_ALLOWED_ORIGINS_SETTINGS
X_FRAME_OPTIONS = X_FRAME_OPTIONS_SETTINGS

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'user_api.User'
APPEND_SLASH = True

FRONTEND_BASE_URL = FRONTEND_BASE_URL_SETTINGS

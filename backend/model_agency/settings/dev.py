"""Django configurations during Development"""
import os

from .base import BASE_DIR

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

BASE_URL = "http://127.0.0.1:8000"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = 'static/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

ALLOWED_HOSTS = [
    "localhost", "127.0.0.1",
    "host.docker.internal", "0.0.0.0",
    "localhost", "3000",
    "testserver"
]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = (
    'django-insecure-l9#bl+e34vxq_#mioo2*c7#+6v^a$w@7l6@_@v1_-ywujxllo1'
)

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# CORS_ALLOWED_ORIGINS = [
#     "http://127.0.0.1:3000"  # Replace with frontend URL
# ]

# OR: Allow all origins during development (not recommended for production)
CORS_ALLOW_ALL_ORIGINS = True  # Change to False if you want to allow specific

# Celery configurations during development and testing
# using Docker memery as broker
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}

# Email configurations
# prints all emails to a terminal, not actually sending emails
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

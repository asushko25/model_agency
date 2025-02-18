"""Django configurations during Development"""
from .base import BASE_DIR

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

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

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:3000/",  # Replace with frontend URL
]

# Celery configurations during development and testing
# using Docker memery as broker
CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}

# Email configurations
# prints all emails to a terminal, not actually sending emails
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

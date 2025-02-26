"""Django configurations during Development"""
from .base import BASE_DIR, config
import core.cloudflare.settings

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

BASE_URL = "http://127.0.0.1:8000"

# MEDIA_URL = f"{BASE_URL}/media/"

# configure Cloudflare R2 S3 storages for media and static files
STORAGES = {
    "default": {
        "BACKEND": "core.cloudflare.storages.MediaFileStorage",
        "OPTIONS": core.cloudflare.settings.CLOUDFLARE_R2_CONFIG_OPTIONS
    },
    "staticfiles": {
        "BACKEND": "core.cloudflare.storages.StaticFileStorage",
        "OPTIONS": core.cloudflare.settings.CLOUDFLARE_R2_CONFIG_OPTIONS,
    }
}


# configurations for boto3 it seems like configurations for django-storages
# and boto3 are separate
AWS_STORAGE_BUCKET_NAME = config("CLOUDFLARE_R2_BUCKET")
AWS_S3_SECRET_ACCESS_KEY = config("CLOUDFLARE_R2_SECRET_KEY")
AWS_S3_ACCESS_KEY_ID = config("CLOUDFLARE_R2_ACCESS_KEY")
AWS_S3_ENDPOINT_URL = config("CLOUDFLARE_R2_BUCKET_ENDPOINT")
AWS_QUERYSTRING_AUTH = True
AWS_QUERYSTRING_EXPIRE = 7200
AWS_S3_SIGNATURE_VERSION = "s3v4"

# STATIC_URL = f"{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/static/"
MEDIA_URL = f"{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/media/"


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

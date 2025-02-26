"""Django configurations during Production"""

from .base import config
import dj_database_url

import sentry_sdk
# In Sentry, profiling refers to tracking and analyzing the performance
# of your code. This involves collecting data on how long different parts
# of your application take to execute, such as:

# Functions
# Database queries
# Middleware processing
# API calls
from sentry_sdk.integrations.django import DjangoIntegration

import core.cloudflare.settings

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = config("DJANGO_ALLOWED_HOSTS").split()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

CORS_ALLOWED_ORIGINS = config("DJANGO_CORS_ALLOWED_ORIGINS").split()

# Ensures CSRF protection is only over HTTPS
CSRF_COOKIE_SECURE = True

# Forces secure connection, Users may connect insecurely
# making them vulnerable to MITM attacks
SECURE_SSL_REDIRECT = True

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(
        default=config("DATABASE_URL"),
        conn_max_age=300  # 5-minute persistent connection
    )
}

# Celery configurations
CELERY_BROKER_URL = config("REDIS_URL") + "/0"

# Email configurations

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_PORT = config("EMAIL_PORT")
EMAIL_USE_SSL = False
EMAIL_USE_TLS = True


# Cache configurations
CACHE = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": config("REDIS_URL") + "/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.HerdClient",
            "IGNORE_EXCEPTIONS": True,
            "CONNECTION_POOL_KWARGS": {"max_connection": 100}
        },
        "TIMEOUT": 60 * 10  # cache timeout is 10 minutes
    }
}

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

STATIC_URL = f"{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/static/"
MEDIA_URL = f"{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/media/"

# Configure Sentry SDK performance monitoring server
# with integration with Django
# https://docs.sentry.io/platforms/python/integrations/django/
SENTRY_DSN = config("SENTRY_DSN")

if SENTRY_DSN:
    sentry_sdk.init(
        dsn=config("SENTRY_DSN"),
        integrations=[
            DjangoIntegration(
                # How to name transactions that show up in Sentry tracing.
                # "/myproject/myview/<foo>" if you set transaction_style="url".
                # "myproject.myview" if you set transaction_style="function_name".
                transaction_style="url",
                # Create spans and track performance of all middleware in your Django project.
                middleware_spans=True,
                # Create spans and track performance of all synchronous Django
                # signals receiver functions in your Django project
                signals_spans=False,
            )
        ],
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for tracing.
        traces_sample_rate=1.0,
        _experiments={
            # Set continuous_profiling_auto_start to True
            # Sentry will automatically start collecting performance
            # profiling data whenever possible
            "continuous_profiling_auto_start": True,
        }
    )

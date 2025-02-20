"""Django configurations during Production"""

import os

import dj_database_url


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS").split(" ")

CORS_ALLOWED_ORIGINS = os.getenv("DJANGO_CORS_ALLOWED_ORIGINS").split()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Ensures CSRF protection is only over HTTPS
CSRF_COOKIE_SECURE = True

# Forces secure connection, Users may connect insecurely
# making them vulnerable to MITM attacks
SECURE_SSL_REDIRECT = True

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(
        default=os.getenv("DATABASE_URL"),
        conn_max_age=300  # 5-minute persistent connection
    )
}


# Celery configurations
CELERY_BROKER_URL = os.getenv("REDIS_URL") + "/0"

# Email configurations
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_USE_SSL = False
EMAIL_USE_TLS = True


# Cache configurations
CACHE = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.getenv("REDIS_URL") + "/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.HerdClient",
            "IGNORE_EXCEPTIONS": True,
            "CONNECTION_POOL_KWARGS": {"max_connection": 100}
        },
        "TIMEOUT": 60 * 10  # cache timeout is 10 minutes
    }
}

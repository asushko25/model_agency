"""Django configurations during Production"""

import os


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS").split(" ")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "PORT": os.getenv("POSTGRES_PORT"),
        # Persistent connections reduce the overhead of reopening connections.
        "CONN_MAX_AGE": os.getenv("POSTGRES_CONN_MAX_AGE", 300),
    }
}

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
        "LOCATION": os.getenv("DJANGO_REDIS_CACHE_URL"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.HerdClient",
            "IGNORE_EXCEPTIONS": True,
            "CONNECTION_POOL_KWARGS": {"max_connection": 100}
        },
        "TIMEOUT": 60 * 10  # cache timeout is 10 minutes
    }
}

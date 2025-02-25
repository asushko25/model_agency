from .base import *

DJANGO_ENV = config("DJANGO_ENV")

if DJANGO_ENV == "production":
    from .prod import *
elif DJANGO_ENV == "staging":
    from .staging import *
else:
    from .dev import *

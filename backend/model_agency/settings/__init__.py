import os
from dotenv import load_dotenv

from .base import *

load_dotenv()

DJANGO_ENV = os.getenv("DJANGO_ENV")

if DJANGO_ENV == "production":
    from .prod import *
elif DJANGO_ENV == "staging":
    from .staging import *
else:
    from .dev import *

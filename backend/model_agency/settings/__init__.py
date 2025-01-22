import os
from dotenv import load_dotenv

from .base import *

load_dotenv()

if os.getenv("DJANGO_ENV") == "production":
    from .prod import *
else:
    from .dev import *

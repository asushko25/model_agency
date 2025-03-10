"""
    Common variables used in our Locust testing
"""
from dotenv import load_dotenv

import faker

import os

from locust.contrib.fasthttp import FastHttpSession

from requests import Session as RequestSession

from typing import TypeAlias

load_dotenv()

# constance are URI can be also used for grouping requests
MAIN_PAGE = "model/main/"
MAN_PAGE = "model/man/"
WOMAN_PAGE = "model/woman/"
CONTACT_PAGE = "contact/"


# variables which are going to be used in grouping requests
# for dynamic URL pages, for example when searching or filtering
# getting specific model. Grouping allows better reports and statistics
MODEL_DETAIL_GROUP = "model/<...>/<model_id>"
CONTACT_MODEL_GROUP = "contact/<model_id>"

# I found it difficult to generate consecutive valid phone numbers
# so we are using one valid phoCne number
PHONE_NUMBER = "+1-605-531-2075"
HOST = os.getenv("LOCUST_ATTACK_HOST", "http://127.0.0.1:8000/")

# pagination util, maximum number of records on one page
LIMIT = 6

HttpSessionType: TypeAlias = FastHttpSession | RequestSession

fake = faker.Faker()
